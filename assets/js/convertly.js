$(document).ready(function() {
	bindevents();
	init();
	// You should definitely change the google tracking code below.
	$.ga("UA-8284931-1",	{selectorMap:	{'#convert':'/convertdoc',
									  		 '#download':'/downloaddoc'
									 		}
							});
});

function init(){
	ghost(new Array('#step2','#step3'), 1);
	checksections();
}

function bindevents(){
	$('*').unbind();
	$('input').change(checksections);
	$('input').keyup(checksections);
	$('#convert').click(convert);
	$('#upload_form').ajaxForm(callback);
}

function convert(){
	if (!validate()){ return false;}
	$('#errors').remove();
	$('#step2').append('<p class="processing">Processing</p>');
	$('#upload_form').submit();
}

function callback(result, status){
    //console.log(result);
	result = result.split(':');
	status = result[0];
	result = result.slice(1).join(':');
	if(status == 'success'){
		var id = result;
		$('.processing').remove();
		$('#download').attr('href', 'download/' + id);
		$('.convert_button').addClass("done");
		$('.convert_button a').hide();
		unghost(new Array('#step3'), 1000);
	}
	else{
		var error = 'An unknown error has occurred';
		if (status == 'error'){ error = result;}
		$('.processing').remove();
		$('#step2').append('<p id="errors">' + error + '</p>');
	}
}

function validate(){
	var document = $('#id_file').attr('value');
	if (fields = fields_notvalid()){
		alert('The following fields are required to submit: ' + fields);
		return false;
	}
	if (filetype_notvalid(document, 'docx') && filetype_notvalid(document, 'zip')){
		alert("The file '" +document+ "' does not appear to be a valid filetype");
		return false;
	}
	return true;
}

function fields_notvalid(){
	var document = $('#id_file').attr('value');
	
	fields = new Array();
	if (!document){ fields.push('File');}
	
	if (fields.length){ return fields;}
	else              { return false;}
}

function filetype_notvalid(filename, validext){
	extension  = filename.split('.').pop();
	reg        = new RegExp(validext, ["i"]);
	return !Boolean(extension.match(reg));
}

function checksections(){
	$('.convert_button').removeClass('done');
	$('.convert_button a').show();
	var document = $('#id_file').attr('value');	
	if (document){ unghost(new Array('#step2'), 1000);}
}

function ghost(selectors, speed){
	selector = selectors.pop()
	$(selector + ' *').fadeTo(speed, .5);
	$(selector + ' input').attr("disabled", "disabled");
	$(selector + ' button').attr("disabled", "disabled");
	$(selector + ' .waiting').show();
	$(selector + ' .result').hide();
	
	if (selectors.length > 0){ghost(selectors, speed);}
	else                     {return true;}
}

function unghost(selectors, speed){
	selector = selectors.pop()
	$(selector + ' *').fadeTo(speed, 1);
	$(selector + ' input').removeAttr("disabled");
	$(selector + ' button').removeAttr("disabled");
	$(selector + ' .waiting').hide();
	$(selector + ' .result').show();
	
	if (selectors.length > 0){unghost(selectors, speed);}
	else                     {return true;}
}