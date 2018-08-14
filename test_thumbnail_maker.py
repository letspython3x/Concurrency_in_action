from concurrency.thumbnail_maker import ThumbnailMakerService

IMG_URLS = \
    ['http://www.gunnerkrigg.com//comics/00000001.jpg',
     'http://www.gunnerkrigg.com//comics/00000002.jpg',
     'http://www.gunnerkrigg.com//comics/00000003.jpg',
     'http://www.gunnerkrigg.com//comics/00000004.jpg',
     'http://www.gunnerkrigg.com//comics/00000005.jpg',
     'http://www.gunnerkrigg.com//comics/00000006.jpg',
     'http://www.gunnerkrigg.com//comics/00000007.jpg',
     'http://www.gunnerkrigg.com//comics/00000008.jpg',
     'http://www.gunnerkrigg.com//comics/00000009.jpg',
     'http://www.gunnerkrigg.com//comics/00000010.jpg',
     'http://www.gunnerkrigg.com//comics/00000011.jpg',
     'http://www.gunnerkrigg.com//comics/00000012.jpg',
     'http://www.gunnerkrigg.com//comics/00000013.jpg',
     'http://www.gunnerkrigg.com//comics/00000014.jpg',
     'http://www.gunnerkrigg.com//comics/00000015.jpg',
     'http://www.gunnerkrigg.com//comics/00000016.jpg',
     'http://www.gunnerkrigg.com//comics/00000017.jpg',
     'http://www.gunnerkrigg.com//comics/00000018.jpg',
     'http://www.gunnerkrigg.com//comics/00000019.jpg',
     'http://www.gunnerkrigg.com//comics/00000020.jpg',
     ]


def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
