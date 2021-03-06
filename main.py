import common
import confirm_use

def compare(path1, path2):
    # 刪除已有的資料夾重新創建
    musicPath = common.folderRemake()
    # process start
    common.filterOther(path1)
    fileName1 = common.fileNameCatch(path1)
    tempPath1 = common.pathSplice(musicPath, fileName1)
    common.mkMusicDir(tempPath1, "mp3")
    common.mkMusicDir(tempPath1, "wav")
    mp3FilePath1 = common.transferMP3(path1, tempPath1)
    wavFilePath1 = common.transferWAV(path1, tempPath1)
    mp3FileList1 = common.sortList(mp3FilePath1)
    wavFileList1 = common.sortList(wavFilePath1)
    assert len(mp3FileList1) == len(wavFileList1), "numbers of file not equal"
    mp3Data1, wavData1 = common.parseMusic(mp3FileList1, wavFileList1)
    curList1 = common.dataSplice(mp3Data1, wavData1)
    # ----------------------------------------------------------------------
    common.filterOther(path2)
    fileName2 = common.fileNameCatch(path2)
    tempPath2 = common.pathSplice(musicPath, fileName2)
    common.mkMusicDir(tempPath2, "mp3")
    common.mkMusicDir(tempPath2, "wav")
    mp3FilePath2 = common.transferMP3(path2, tempPath2)
    wavFilePath2 = common.transferWAV(path2, tempPath2)
    mp3FileList2 = common.sortList(mp3FilePath2)
    wavFileList2 = common.sortList(wavFilePath2)
    assert len(mp3FileList2) == len(wavFileList2), "numbers of file not equal"
    mp3Data2, wavData2 = common.parseMusic(mp3FileList2, wavFileList2)
    curList2 = common.dataSplice(mp3Data2, wavData2)
    # ----------------------------------------------------------------------
    confirmList = confirm_use.get_confirm_fftdata(curList1, curList2)
    common.createLog(confirmList)

if __name__ == '__main__':
    path1 = r"C:\Users\marrash_kao\Desktop\tools\music-test\tu001"
    path2 = r"C:\Users\marrash_kao\Desktop\tools\music-test\tu002"
    compare(path1, path2)