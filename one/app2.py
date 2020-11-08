from flask import Flask,render_template,request,redirect,url_for,Response
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test3.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
class users(db.Model):
    __tablename__ = 'user1'
    id = db.Column( db.String(20), primary_key = True)
    to=db.Column(db.String(100))
    from1=db.Column(db.Integer)

    def __init__(self, id, to, from1):
        self.id=id
        self.to=to
        self.from1=from1

class tts(db.Model):
    __tablename__ = 'tt1'
    name = db.Column(db.Integer, primary_key = True)
    number=db.Column(db.Integer)

    def __init__(self, name,number):
        self.name=name
        self.number=number
db.create_all()


@app.route('/')
def hello_world():
    # user=users('001',0,0)
    # db.session.add(user)
    # db.session.commit()
    # print(1)
    # print(users.query.all())
    for i in range(1,12):
        if tts.query.filter_by(name=i).all():
            continue
        else :
            tt=tts(i,0)
            db.session.add(tt)
            db.session.commit()
            print(i,'success')
    return render_template('log1.html')


@app.route('/jump/<id>',methods=['GET','POST'])
def jump(id):
    id=int(id)
    if id==1:  #点击登录跳转
        print(request.form['id'], '1111\n')
        if request.form['id'] == "teacher":

            return render_template('search.html',user1=users.query.all())
        if not request.form['id'] or not request.form['from']:
            return render_template('error.html')
        else:
            id=request.form['id']
            from1=request.form['from']
            # user = users.query.filter_by(id=id).first()
            # user.from1=int(from1)
            # db.session.commit()

            if users.query.filter_by(id=id).all():
                print("数据库已存在用户\n")
                print(type(users))
                user=users.query.filter_by(id=id).first()
                print(user.id,user.to,user.from1)
                if(user.to!=''):
                    return render_template('error1.html')

            else:
                print("新用户注册\n")
                user=users(id,'',int(from1))
                db.session.add(user)
                db.session.commit()
        return render_template('home.html',uid=id)
    elif id==2:  #返回首页
        return render_template('log1.html')
    elif id==3:
        return render_template('search.html', user1=users.query.all())
        # pass
        # to1=0
        # for i in range(1,12):
        #     att='hobby'+str(i)
        #     # print(att)
        #     try:
        #         if not request.form[att]:
        #             continue
        #         print(request.form[att], '1111\n')
        #         if to1==0:
        #             to1=i
        #         else :
        #             print('fail\n')
        #             return render_template('error2.html')
        #     except:
        #         pass
        # user = users.query.filter_by(id=id).first()
        # user.to=to1
        # db.session.commit()
        # return render_template('success.html')
    elif id==4:
        pass
        # return render_template('home.html',uid=id)

@app.route('/jump2/<id>',methods=['GET','POST'])
def jump2(id):
    to1 = 0
    user = users.query.filter_by(id=id).first()
    for i in range(1,12):
        att = 'hobby' + str(i)
        try:
            if not request.form[att]:
                continue
            if i==user.from1:
                return render_template('error3.html',uid=id)
        except:
            pass
    for i in range(1, 12):
        att = 'hobby' + str(i)
        # print(att)
        try:
            if not request.form[att]:
                continue
            print(request.form[att], '1111\n')
            # if i==user.from1:
            #     return render_template('error3.html',uid=id)
                # return render_template('index.js', uid=id)
            user.to=user.to+str(i)+' '
            tt = tts.query.filter_by(name=to1).first()
            tt.number = tt.number + 1
            print(tt.number, '11')
            db.session.commit()
        except:
            pass
    print(user.to)
    db.session.commit()
    # user.to = to1
    # print(to1)    #注意取消注释
    # db.session.commit()
    # tt=tts.query.filter_by(name=to1).first()
    # tt.number=tt.number+1
    # print(tt.number,'11')
    # db.session.commit()
    return render_template('success.html')

@app.route('/jump3/<id>',methods=['GET','POST'])
def jump3(id):
    print(id)
    return render_template('home.html',uid=id)



@app.route('/search/',methods=['GET','POST'])
def search():  #查找数据库票数
    tid=request.form['tid']
    print(tid)
    return render_template('search.html', user1=users.query.filter_by(id=tid).all())


if __name__ == '__main__':
    app.run(debug=True)
