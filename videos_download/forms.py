from django import forms


class YoutubeForm(forms.Form):
    url = forms.URLField(label="Enter Youtube Url: ")
