## Downloader Youtube 

This library was created to create a YouTube download link, you can get the download link of that video in different formats by sending the original link of the video from the YouTube site.  
You can use this library in web or desktop or mobile projects, etc. according to the information below.  
Note: There is no prerequisite.

---

## How it works?

Use the following command to **install this library**

```python
pip install YTDPersian
```

**Link preparation:** Send the video link to the library

input : string

output : no

```python
from YTDPersian import download
var = download("URL")
```

**Option :** Information you can get through this library

1.  Information Video
2.  Quality Video
3.  Link Download

**1\. Information Video**

This method has an input, the name of this input is ‘**List**’, if it is false, the output is returned as a string; If it is true, the output is returned as a list of the dictionary. It is false by default, so we can leave nothing as input.

List = False

```python
from YTDPersian import download
var = download("URL")
get_info = var.InfoVideo()
print(get_info)
_______ output ________
Title : {textTitle}     -     Durition : {textDescription}
Url : {textUrl}
```

List = True

```python
from YTDPersian import download
var = download("URL")
get_info = var.InfoVideo(True)
print(get_info)
_______ output ________
[{ 'Title' : {textTitle}, 'Durition' : {textDescription}, 'Url' : {textUrl} }]
```

**2\. Quality Video**

This method has an input, the name of this input is ‘**List**’, if it is false, the output is returned as a string; If it is true, the output is returned as a list of the dictionary. It is false by default, so we can leave nothing as input.

List = False

```python
from YTDPersian import download
var = download("URL")
get_quality = var.ShowQuality()
print(get_info)
_______ output ________
Type : mp4  Quality : 360 Audio : Yes
Type : mp4  Quality : 720 Audio : Yes
...
```

List = True

```python
from YTDPersian import download
var = download("URL")
get_quality = var.ShowQuality(True)
print(get_info)
_______ output ________
[
{ 'Type' : {textType}, 'Quality' : {textQuality}, 'Audio' : {textStatusAudio} },
{ 'Type' : {textType}, 'Quality' : {textQuality}, 'Audio' : {textStatusAudio} },
{ 'Type' : {textType}, 'Quality' : {textQuality}, 'Audio' : {textStatusAudio} },
...
]
```

**3\. Link Download**

This method has two inputs, one input as "**type**" and one input as "**quality**". To get the download link, you must send the file type and video quality as a string to this method so that the download link will be sent to you. Display, if you do not enter the type and quality correctly, you will receive the text "**No Result**".

```python
from YTDPersian import download
var = download("URL")
get_link = var.GetLink("{TypeVideo}", "{QualityVideo}")
print(get_link)
_______ output ________
"{textLinkDownload}"
```

The great scientific and educational collection of the [**SARZAMIN DANESH**](https://lssc.ir) thanks you.
