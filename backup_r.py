import os
import shutil
#import filecmp
# from collections import Counter
import timeit


def LocationContent(location: object, MovieExt: object = ["mp4", "m4v"]) -> object:
    """

    :param location:
    :param MovieExt:
    :return:
    """
    movies = []
    gen = os.walk(location)
    for root, dirs, files in gen:
        for file in files:
            if file[-3:].lower() in MovieExt:
                movie = [root, file]
                movies.append(movie)
    return movies


def DiffContent(source: str, destination: str) -> list:
    """

    :param source:
    :param destination:
    :return:
    """
    source  = LocationContent(source)
    destination = LocationContent(destination)

    sourcetitles = [movie[1] for movie in source]
    destinationtitles = [movie[1] for movie in destination]

    inter = list(set(sourcetitles).difference(set(destinationtitles)))

    res = []
    for movie in inter:
        indices = [i for i, x in enumerate(sourcetitles) if x == movie]
        if len(indices) > 1:
            print(movie)
            print(len(indices))
        tmp = [movie, [source[i][0] for i in indices]]
        res.append(tmp)
    return res


def _check_path(path):
    if path[-1] != "/":
        path = path + "/"
    return path

def CopyMovies(source: str, destination: str) -> list:
    """

    :param source:
    :param destination:
    :return:
    """
    start_prog = timeit.default_timer()

    MoviesToCopy = DiffContent(source, destination)
    source = _check_path(source)
    destination = _check_path(destination)
    NbMoviesToCopy = len(MoviesToCopy)

    print("There are {} movies to copy\n".format(NbMoviesToCopy))

    for i, movie in enumerate(MoviesToCopy):
        start = timeit.default_timer()
        print("starting copy of movie # {} out of {}".format(*[i + 1, NbMoviesToCopy]))
        print("starting copy of {}".format(movie[0]))
        src = movie[1][0] + "/" + movie[0]
        dest = destination + movie[0]
        shutil.copyfile(src, dest)
        print("Movie {} is copied\n".format(movie[0]))
        stop = timeit.default_timer()
        print('Time: ', stop - start)

    print("{} Movies has been copied from {} {}".format(*[MoviesToCopy, source, destination]))

    stop_prog = timeit.default_timer()

    print("This program has been running for {}".format((stop_prog - start_prog)))

    return MoviesToCopy


def FolderStructure(source, destination):
    """
    Creta folder strucuture
    :param source:
    :param destination:
    :return:
    """
    source = _check_path(source)
    destination = _check_path(destination)
    z = len(source)
    folderssource = [destination + folder[z:] for (folder, _, _) in os.walk(source)]
    foldersdestination = [folder for (folder, _, _) in os.walk(destination)]
    folderstocreate = list(set(folderssource).difference(set(foldersdestination)))
    folderstodelete = list(set(foldersdestination).difference(set(folderssource)))

    # create missing folder
    for folder in folderssource:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("{} created".format(folder))
        else:
            files = os.listdir(folder)
            if len(files) != 0:
                print(folder)
                print(files)

    print("\n\n")

    # print the content of non empty folder
    for folder in folderstodelete:
        content = os.listdir(folder)
        print(folder)
        if not content:
            print(content)


    return folderstocreate


if __name__ == "__main__":
    source = "/media/WD_NAS/Shared Videos"
    source = "/media/raspberry"
    source = "/media/SSD_1TB/Videos"
    source = "/mnt/y/"
    destination = "/media/HDD_8TB/Films/"
    destination = "/mnt/j/Videos/"

    #inter = CopyMovies(destination, destination)
    lst = FolderStructure(destination, source)
    for i in lst:
        print(i)



