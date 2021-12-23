from pafy import new
while True:
    url = input('enter your link:')
    video = new(url)
    audio = video.audiostreams
    stream = video.streams
    counter = 1
    # for i in stream:
    #     print(f"{counter}- {i}")
    #     counter += 1
    choise = int(input(
        'to dowmload audio enter 1 \nto dowmload video enter 2 \n your choise: '))
    if choise == 1:
        print("*************")
        for i in audio:
            print(f"{counter}- {i}")
            counter += 1
        print("*************\n")
        index = int(input('enter your audio choise:'))
        index -= 1
        audio[index].download()
    else:
        print("*************")
        for i in stream:
            print(f"{counter}- {i}")
            counter += 1
        print("*************\n")
        index = int(input('enter your video choise:'))
        index -= 1
        stream[index].download()
