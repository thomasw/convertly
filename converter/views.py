from converter        import *
from django.template  import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.http      import HttpResponse, Http404
from converter.forms  import UploadDoc
from zipfile          import ZipFile

def index(request):
	""" Interface for uploading, converting, and downloading documents """
	
	form = UploadDoc()
	return render_to_response('index.phtml', {'form':form}, context_instance=RequestContext(request))
	
def download(request, job_id):
	""" Given a job id will provide the user's browser with a converted archive """
	clean()	
	tmpdir = tempfile.gettempdir()
	jobdir = os.path.join(tmpdir, tmp_prefix + job_id)
	
	#check if job exists
	if not os.path.isdir(jobdir): raise Http404
	
	#find files to zip
	files = get_jobfiles(jobdir)
	
	#create zip archive
	archive = ZipFile(tempfile.mkstemp()[1], 'w')
	for f in files:
		name, arcname = str(f), str(f[len(jobdir) + 1:])
		archive.write(name, arcname)
	archive.close()
	
	#return archive
	f        = file(archive.filename)
	contents = f.read()
	f.close()
	rm(archive.filename)
	filename = os.path.basename(job_id) + '.zip'
	mimetype = 'application/zip'
	response = HttpResponse(contents, mimetype=mimetype)
	response['Content-Disposition'] = 'attachment; filename=%s' % (filename,)
	return response

def upload(request):
	""" Accepts docx files to be converted to html """
	
	if request.method == 'POST':
		clean()
		form = UploadDoc(request.POST, request.FILES)
		if form.is_valid():
			#Move uploaded file to job directory
			upload    = request.FILES['file']
			source    = upload.temporary_file_path()
			jobdir    = tempfile.mkdtemp(prefix=tmp_prefix)
			dest      = os.path.join(jobdir, upload.name)
			os.rename(source, dest)
			
			#Process an individual docx file
			if has_extension(upload.name, 'docx'):
				files = [dest,]
				
			#Process a zip archive, only pulls docx in root dir of archive
			if has_extension(upload.name, 'zip'):
				#read archive
				archive = ZipFile(dest, 'r')
				members = archive.namelist()
				members = filter(lambda f: has_extension(f, 'docx'), members)
				members = filter(lambda f: len(f.split(os.sep)) == 1, members)
				
				if not members: return error('No docx files found in root directory of archive.')
				
				#extract each item
				for m in members:
					try:
						f = file(os.path.join(jobdir,m), 'w')
						f.write(archive.read(m))
						f.close()
					except:
						return error('An error occurred trying to extract files from archive.')
				
				#add docx files to file list
				files = os.listdir(jobdir)
				files = filter(lambda f: f.split('.')[-1] == 'docx', files)
				files = map(lambda f: os.path.join(jobdir, f), files)
			
			#Convert files in job
			for f in files:
				input   = f
				output  = os.path.join(jobdir, remove_ext(f) + '.html')
				im      = 'cdwsiodocx'
				om      = 'cdwsiodocx'
				job = Zombie(input, output)
				if job.convert():
				    job.finalize()
				else:
					e = sys.stderr.last_error()
					return error('There was an error converting the document provided "%s"' % e)
			
			context = {'id': os.path.basename(jobdir)[len(tmp_prefix):]}
			return render_to_response('result.phtml', context)

		return render_to_response('errors.phtml', {'errors':form.errors})
