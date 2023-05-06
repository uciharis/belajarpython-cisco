print("halooo")
# ini snippet: print(__name__) # mencetak nama modul ini jika dijalankan lewat file yang mengimportnya
# mencetak __main__ jika dijalankan langsung dari file ini
counter = 0
if __name__ == "__main__":
    print("i prefer to be a module")
else:
    print("I like tobe a module")