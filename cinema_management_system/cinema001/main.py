from flask import Flask, render_template
import dataprocess
import web_package

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    processor = dataprocess.CinemaData("cinema.db")
    processor.create_tables()
    processor.import_data_from_excel("./sql/customers.xlsm", "customers")
    processor.import_data_from_excel("./dataset/机器人21级补考.xlsx", "resit")

    processor.import_data_from_excel("./dataset/物联网.xlsx","finaltest")
    processor.import_data_from_excel("./dataset/物联网补考.xlsx", "resit")

    processor.import_data_from_excel("./dataset/人工智能21级.xlsx","finaltest")
    processor.import_data_from_excel("./dataset/人工智能21级补考.xlsx", "resit")

    processor.import_data_from_excel("./dataset/数据21级.xlsx","finaltest")
    processor.import_data_from_excel("./dataset/数据21级补考.xlsx", "resit")

    processor.process_data()
    print("process data OK")
    processor.add_user('admin', 'admin', 'admin')
    processor.add_user('teacher', 'teacher', 'teacher')
    processor.add_user('student', 'student', 'student')
    print("add user OK")

    app.run(debug=True, port=8080)
