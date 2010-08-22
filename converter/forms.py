from django import forms

class UploadDoc(forms.Form):
	file = forms.FileField(label="Document", required=True)
