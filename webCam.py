import cv2, time, random, dropbox

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        print(ret)
        command = "photo"+str(number)+".png"
        cv2.imwrite(command,frame)
        result = False
    return(command)
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
        access_token = '1-OYwmvfCo0AAAAAAAAAAfIqP-ed6sPx6e5AKhVxlOV0R-ZuYI6cOiYrSNNrqn30'
        file = img_name
        file_from = file
        file_to = "/photos/"+img_name
        dbx = dropbox.Dropbox(access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
            print("file uploaded")

def main():
    while(True):
        if ((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

main()