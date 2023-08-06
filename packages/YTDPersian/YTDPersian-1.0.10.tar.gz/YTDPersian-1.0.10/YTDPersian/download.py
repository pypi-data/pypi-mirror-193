import requests
class download:
    Json_video = None
    def api_url(self):
        return "https://ssyoutube.com/api/convert"
		
    def __init__(self, ytURL):
        keys ={'url' : ytURL}
        result = requests.post(url = self.api_url(), params = keys)
        self.Json_video = result.json()
		
    def ShowQuality(self, List = False):
        video = self.Json_video
        if List:
            list_quality = []
            for i in range(len(video['url'])):
                audio = "Yeas"
                try:
                    if video['url'][i]['attr']['class'] != "":
                        audio = video['url'][i]['attr']['class']
                except:
                    audio = "Not specified"
                list_quality.append({'Type' : video['url'][i]['type'], 'Quality' : video['url'][i]['quality'], 'Audio' : audio})
            return list_quality
        else:
            str_quality = ""
            for i in range(len(video['url'])):
                audio = "Yes"
                try:
                    if video['url'][i]['attr']['class'] != "":
                        audio = video['url'][i]['attr']['class']
                except:
                    audio = "Not specified"
                str_quality += f"Type : {video['url'][i]['type']} \t Quality : {video['url'][i]['quality']} \t Audio : {audio}\n"
            return str_quality
			
    def GetLink(self, Tvideo, Qvideo):
        video = self.Json_video
        for i in range(len(video['url'])):
            if  video['url'][i]['type'] == Tvideo and video['url'][i]['quality'] == Qvideo:
                return video['url'][i]['url']
        return "No Result ..."
		
    def InfoVideo(self, List = False):
        video = self.Json_video
        if List:
            list_title = [{'Title' : video['meta']['title'], 'Durition' : video['meta']['duration'], 'Url' : video['meta']['source']}]
            return list_title
        else:
            title = f"Title : {video['meta']['title']}     -     Durition : {video['meta']['duration']}\n"
            title += f"Url : {video['meta']['source']}"
            return title


