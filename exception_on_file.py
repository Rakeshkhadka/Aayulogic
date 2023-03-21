def file_editor(path, text):
    try:
        with open(path, 'w') as op:
            try:
                op.write(text)
            except:
                print("Unable to write")
    except:
        print("File does not exists")

file_editor('data.txt', 'helloword')