from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1Dx2qi8jCcE0hUmMnCWBL1i_P89DouS1Z/view?usp=sharing',
                                    dest_path='model/model.h5',
                                    unzip=True)