import core


def run(file_path):
    core.file_to_img(file_path)
    core.imgs_to_file()
    core.clean()


run("Your_File_Name.pdf")
