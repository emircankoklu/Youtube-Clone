from django.shortcuts import render

# Static video data (no database needed)
VIDEOS = [
    {
        'id': 1,
        'title': 'Rıza Tamer - Yan',
        'channel': 'netd müzik',
        'views': '16M',
        'time': '8 ay önce',
        'duration': '2:53',
        'thumbnail': 'https://via.placeholder.com/320x180/333/fff?text=Video+1'
    },
    {
        'id': 2,
        'title': 'Hayrettin ile Kaos Show - 2.Sezon 5.Bölüm | Yılbaşı Özel',
        'channel': 'Hayrettin',
        'views': '5.5M',
        'time': '3 gün önce',
        'duration': '1:14:41',
        'thumbnail': 'https://via.placeholder.com/320x180/ff6b00/fff?text=Video+2'
    },
    {
        'id': 3,
        'title': 'TANZANYA - Göçün İçinde SATIYORLAR (Maalesef KUSTUR)',
        'channel': 'Mert Uzutaş',
        'views': '836 B',
        'time': '7 gün önce',
        'duration': '21:21',
        'thumbnail': 'https://via.placeholder.com/320x180/4CAF50/fff?text=Video+3'
    },
    {
        'id': 4,
        'title': 'Ey Açık',
        'channel': 'Sezer Akçu',
        'views': '28 Mn',
        'time': '6 ay önce',
        'duration': '4:28',
        'thumbnail': 'https://via.placeholder.com/320x180/000/fff?text=Video+4'
    },
    {
        'id': 5,
        'title': 'Film Tadında',
        'channel': 'Film Tadında',
        'views': '2.3M',
        'time': '2 gün önce',
        'duration': '8:45',
        'thumbnail': 'https://via.placeholder.com/320x180/00BCD4/fff?text=Short+1'
    },
    {
        'id': 6,
        'title': '87 Kiloluk Karpuz Kralı Görmeden İnanmayacaksınız',
        'channel': 'Köy Hikayeleri',
        'views': '15M',
        'time': '1 hafta önce',
        'duration': '12:34',
        'thumbnail': 'https://via.placeholder.com/320x180/8BC34A/fff?text=Short+2'
    },
    {
        'id': 7,
        'title': 'Herkes Evlenecek Aile Kuracak Diye Birşey Yok',
        'channel': 'Jasmine',
        'views': '8.9M',
        'time': '3 gün önce',
        'duration': '15:22',
        'thumbnail': 'https://via.placeholder.com/320x180/E91E63/fff?text=Short+3'
    },
    {
        'id': 8,
        'title': 'Ava Yaman O Benim Dünyam',
        'channel': 'Müzik Dünyası',
        'views': '12M',
        'time': '5 gün önce',
        'duration': '3:42',
        'thumbnail': 'https://via.placeholder.com/320x180/9C27B0/fff?text=Short+4'
    },
]


def home(request):
    """Home page view with video grid"""
    context = {
        'videos': VIDEOS,
    }
    return render(request, 'videos/home.html', context)
