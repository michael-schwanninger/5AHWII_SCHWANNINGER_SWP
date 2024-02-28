from flask import Flask, render_template, request, jsonify
from sqlalchemy import Column, Integer, create_engine, Text

from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()
metadata = Base.metadata
engine = create_engine('sqlite:///statistics.sqlite3')
db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property()
app = Flask(__name__)


class Statistics(Base):
    __tablename__ = 'statistics'

    id = Column(Integer, primary_key=True)
    choice_name = Column(Text)
    count = Column(Integer)


def update_statistics_db(choice_name, count):
    existing_statistic = Statistics.query.filter_by(choice_name=choice_name).first()

    if existing_statistic:
        existing_statistic.count = count
    else:
        new_statistic = Statistics(choice_name=choice_name, count=count)
        db_session.add(new_statistic)

    db_session.commit()


@app.route('/upload_statistics', methods=['POST'])
def upload_statistics():
    try:
        data = request.json

        for choice in data:
            count = data[choice]
            update_statistics_db(choice, count)

        return jsonify({"message": "Statistics uploaded successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/view_statistics')
def view_statistics():
    statistics = Statistics.query.all()
    statistics_dict = {stat.choice_name: stat.count for stat in statistics}

    return jsonify(statistics_dict)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)
