from pytube import YouTube as yutub

def download():
	link = input ("\033[1;87m- link youtube : ")
	yt = yutub(link)
	yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	yt.download()
	print(yt.title + " has been successfully downloaded !")


download()