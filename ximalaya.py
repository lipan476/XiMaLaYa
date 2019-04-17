

import requests
import json
from lxml import etree

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/53'
}

def get_track_list(albumid, pageNum):

	trackList = []

	request_url = 'https://www.ximalaya.com/revision/album/getTracksList?albumId='+str(albumid)+'&pageNum='+str(pageNum)

	response = requests.get(request_url,headers=headers)

	result = json.loads(response.text)

	if result['ret'] == 200:
	 	tracks = result['data']['tracks']
	 	for track in tracks:
	 		trackList.append({'trackId':track['trackId'],'title':track['title']})


	return trackList


def get_track_url(trackId):
	url = 'https://www.ximalaya.com/revision/play/tracks?trackIds='+str(trackId)

	response = requests.get(url,headers=headers)

	result = json.loads(response.text)

	if result['ret'] == 200:
		tracksForAudioPlay = result['data']['tracksForAudioPlay']
		if len(tracksForAudioPlay) >0:
			return tracksForAudioPlay[0]['src']


# 下载音频文件
def down_track(url,file):
	response = requests.get(url)

	with open(file,'wb') as f:
		f.write(response.content)



if __name__ == '__main__':
	#albumid = 7620048#红楼梦
	albumid = 15273276
	pageNum = 1

	for pageNum in [1,2]:
		trackList = get_track_list(albumid,pageNum)
		print(len(trackList))

		dir = './Audio/'

		for track in trackList:
			trackUrl = get_track_url(track['trackId'])
			if trackUrl:
				print(trackUrl)
				ext = trackUrl[trackUrl.rindex('.'):]
				audioName = track['title']
				file_path = dir+audioName+str(ext)

				#
				#down_track(trackUrl,file_path)
			

