import threading
import time

class Downloadfile(threading.Thread):
    def __init__(self, file_url, save_path)
        threading.Thread.__init__(self)
        self.file_url = file_url, save_path):
        self.save_path = save_path

        def run(self):
            time.sleep(3)
            print(f"download {self.file.url} to {self.save_path}")
            
download_thread = DownloadFile('http://example.com/file.zip', '/path/to/save/file.zip')
download_thread.start()
print('The main program continues to run in foreground.')

# Wait for the download to finish
download_thread.join()
print('Main program waited until download was done.')