import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/direction')
def direction():
    return flask.render_template('direction.html')


@app.route('/tour/<tour_id>')
def tours1(tour_id):
    tours_name = {
        1: "Измайлово Альфа",
        2: "Измайлово Бета",
        3: "Славянка",
        4: "Отель «Москва»",
        5: "А Отель Фонтанка",
        6: "Апарт-отель Вертикаль",
        7: "Adaaran Select Hudhuranfushi",
        8: "Equator Village (ех. Ocean Reef)",
        9: "Kaani Beach Hotel"
    }
    tours_price = {
        1: "15499 р. за 2 людей",
        2: "14656 р. за 2 людей",
        3: "14614 р. за 2 людей",
        4: "11560 р. за 2 людей",
        5: "5892 р. за 2 людей",
        6: "12596 р. за 2 людей",
        7: "482690 р. за 2 людей",
        8: "408109 р. за 2 людей",
        9: "334807 р. за 2 людей"
    }
    tours_description1 = {
        1: "4 звезды",
        2: "3 звезды",
        3: "3 звезды",
        4: "4 звезды",
        5: "3 звезды",
        6: "3 звезды",
        7: "4 звезды",
        8: "3 звезды",
        9: "... звезды"
    }
    tours_description2 = {
        1: "Бесплатный Wi-Fi",
        2: "Бесплатный Wi-Fi",
        3: "Бесплатный Wi-Fi",
        4: "Бесплатный Wi-Fi",
        5: "Бесплатный Wi-Fi",
        6: "Бесплатный Wi-Fi",
        7: "Северный Мале",
        8: "Адду атолл",
        9: "Маафуши"
    }
    tours_description3 = {
        1: "Оценка: 8,6",
        2: "3Оценка: 7,7",
        3: "Оценка: 9,0",
        4: "Оценка: 8,5",
        5: "Оценка: 7,8",
        6: "Оценка: 9,1",
        7: "Оценка: 8,5",
        8: "Оценка: 8,8",
        9: "Оценка: 9,1"
    }
    tours_description4 = {
        1: "60 отзывов",
        2: "83 отзывов",
        3: "33 отзывов",
        4: "78 отзывов",
        5: "14 отзывов",
        6: "23 отзывов",
        7: "172 отзывов",
        8: "54 отзывов",
        9: "3 отзывов"
    }
    tours_image = {
        1: "/static/css/images/1.1.webp",
        2: "/static/css/images/1.2.jpg",
        3: "/static/css/images/1.3.jpg",
        4: "/static/css/images/2.1.jpg",
        5: "/static/css/images/2.2.webp",
        6: "/static/css/images/2.3.jpg",
        7: "/static/css/images/3.1.jpg",
        8: "/static/css/images/3.2.jpg",
        9: "/static/css/images/3.3.jpg"
    }
    tours_site = {
        1: "https://tours.tutu.ru/hotel/9320/?departure=58&hotel_ids%5B%5D=9320&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679197370203&session_hash=213018624",
        2: "https://tours.tutu.ru/hotel/7269/?departure=58&hotel_ids%5B%5D=7269&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679197856329&session_hash=84391936",
        3: "https://tours.tutu.ru/hotel/11023/?departure=58&hotel_ids%5B%5D=11023&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679197853215&session_hash=1904088688",
        4: "https://tours.tutu.ru/hotel/10119/?departure=58&hotel_ids%5B%5D=10119&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679198832519&session_hash=2087490560",
        5: "https://tours.tutu.ru/hotel/10875/?departure=58&hotel_ids%5B%5D=10875&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679198841985&session_hash=1758129152",
        6: "https://tours.tutu.ru/hotel/67557/?departure=58&hotel_ids%5B%5D=67557&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=7&arrival_type=country&time_started=1679198843343&session_hash=1313929216",
        7: "https://tours.tutu.ru/hotel/2908/?departure=58&hotel_ids%5B%5D=2908&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=125&arrival_type=country&time_started=1679199593513&session_hash=164815504",
        8: "https://tours.tutu.ru/hotel/3741/?departure=58&hotel_ids%5B%5D=3741&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=125&arrival_type=country&time_started=1679199599102&session_hash=730003456",
        9: "https://tours.tutu.ru/hotel/67469/?departure=58&hotel_ids%5B%5D=67469&date_begin=24.03.2023&date_end=30.03.2023&nights_min=5&nights_max=9&adults=2&children=0&arrival_id=125&arrival_type=country&time_started=1679199605958&session_hash=1045827736"
    }
    tour_name = tours_name[int(tour_id)]
    tour_price = tours_price[int(tour_id)]
    tour_description1 = tours_description1[int(tour_id)]
    tour_description2 = tours_description2[int(tour_id)]
    tour_description3 = tours_description3[int(tour_id)]
    tour_description4 = tours_description4[int(tour_id)]
    tour_image = tours_image[int(tour_id)]
    tour_site = tours_site[int(tour_id)]
    return flask.render_template('tour.html', tour_name=tour_name, tour_price=tour_price,
                                 tour_description1=tour_description1, tour_description2=tour_description2,
                                 tour_description3=tour_description3, tour_description4=tour_description4,
                                 tour_site=tour_site, tour_image=tour_image)


if __name__ == "__main__":
    app.run(debug=True)
