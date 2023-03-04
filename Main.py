import core

'''
Executes necessary functions in systematic way
'''
def run(outfile="output.pdf"):
    file_src = core.file_pick()
    core.file_to_img(file_src)
    core.imgs_to_file()
    core.clean()

run()
