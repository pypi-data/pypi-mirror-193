import setuptools

setuptools.setup(
    name = "jsong",
    version = "0.9",
    author = "OakTree",
    author_email = "thefirstoaktree@gmail.com",
    description = "Transforms website data from allmusic.com into programmatically usable json and excel files",
    long_description = "jsong streamlines the process of copying data into json files\n\n Valid FILETYPEs: JSON ('.json') and Excel ('.xlsx')\n\nFor discographies: \n\tPick a link of your choice (e.g., https://www.allmusic.com/artist/taylor-swift-mn0000472102/discography, https://www.allmusic.com/artist/elton-john-mn0000796734/discography, etc.) and pass the url to the function getDiscography(URL_HERE, FILE_TYPE_HERE)\n\nFor albums: \n\t Pick a link of your choice (https://www.allmusic.com/album/innervisions-mw0000192406, https://www.allmusic.com/album/a-night-at-the-opera-mw0000391519, etc.) and pass the url to the function getAlbum(URL_HERE, FILE_TYPE_HERE)\n\nData is collected in part with the use of a Selenium webdriver. Web pages will be periodically opened and closed in order to webscrape information; please do not close these pages -- they will be automatically closed when the code has been executed. Thank you :)\n\nNOTE: Jsong version 0.8 takes significantly longer to process full discographies, but is more user-friendly. For a quicker process, please download Jsong version 0.7.",
    long_description_content_type = "text/markdown",
    dependencies = [
    "selenium",
    "time",
    "bs4",
    "xlsxwriter",
    "colorama"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)