from flask import render_template
# //导入蓝本 main
import time
import json
from datetime import datetime
from . import main
from .models import User, Task
from . import db
from flask import jsonify, redirect, url_for, request, session
import datetime
from flask_login import login_required, logout_user, login_user, current_user
from datetime import date, timedelta


@main.route('/')
@main.route('/index')
@login_required
def index():
    user = current_user
    date_list = []
    result = []
    for i in range(8):
        date_list.append((date.today() + timedelta(days=i)).strftime("%Y-%m-%d"))
    for i in range(len(date_list) - 1):
        # tasks = Task.objects.filter(begin__range=(date_list[i], date_list[i+1]))
        start = datetime.datetime.strptime(date_list[i], "%Y-%m-%d")
        end = datetime.datetime.strptime(date_list[i+1], "%Y-%m-%d")
        tasks = Task.query.filter(Task.begin < end).filter(Task.begin >= start).filter(Task.user_id == user.id)
        # print("====")
        # print(tasks)
        # tasks = Task.objects.filter(user=user, begin__gte=date_list[i], begin__lt=date_list[i + 1])
        tmp = [date_list[i]]
        for i in range(0, 24):
            tmp.append("")
        for task in tasks:
            index = int(task.begin_time.split(":")[0])
            last_name = task.name
            # print(task.priority)
            if task.priority == "Higher":
                last_name = '<div onclick="showWin(\'' + task.description + '\')"><div style="color: red">' + last_name + '</div></div>'
            elif task.priority == "Medium":
                last_name = '<div onclick="showWin(\'' + task.description + '\')"><div style="color: blue">' + last_name + '</div></div>'
            elif task.priority == "Lower":
                last_name = '<div onclick="showWin(\'' + task.description + '\')"><div style="color: green">' + last_name + '</div></div>'
            else:
                pass
            tmp[index + 1] = tmp[index + 1] + last_name + "\n"
        result.append(tmp)

    ar2 = list(map(list, zip(*result)))
    heads = [""]
    heads.extend(ar2[0])
    for i in range(0, 12):
        # print("=====")
        # print(i)
        # print(ar2[i + 1])
        # print(str(i) + ":00~" + str(i + 1) + ":00")
        tmp_list = ar2[i + 1].copy()
        new_list = ["<span style='font-size:30pt; font-family: Arial, Helvetica, sans-serif;'>" + str(i) + "</span>" + " a.m."]
        new_list.extend(tmp_list)
        # print(new_list)
        ar2[i + 1] = new_list
        # print(ar2[i + 1])
    for i in range(0, 12):
        # print("=====")
        # print(i)
        # print(ar2[i + 1])
        # print(str(i) + ":00~" + str(i + 1) + ":00")
        tmp_list = ar2[i + 13].copy()
        if i == 0:
            new_list = ["<span style='font-size:30pt; font-family: Arial, Helvetica, sans-serif;'>12</span>" + " p.m."]
        else:
            new_list = ["<span style='font-size:30pt; font-family: Arial, Helvetica, sans-serif;'>" + str(i) + "</span>" + " p.m."]
        new_list.extend(tmp_list)
        # print(new_list)
        ar2[i + 13] = new_list
        # print(ar2[i + 1])
    result = ar2
    del result[0]
    # print(result)
    return render_template('index.html', current_user=current_user, heads=heads, result=result)

@main.route('/add_task', methods=['POST', 'GET'])
@login_required
def add_task():
    print(request.method)
    if request.method == 'GET':
        return render_template('add_task.html', current_user=current_user)
    if request.method == 'POST':
        user = current_user
        print("----")
        name = request.form.get('name')
        begin = request.form.get('begin')
        priority = request.form.get('priority')
        description = request.form.get('description')
        print(name)
        print(begin)
        print(priority)
        print(description)

        begin_date = ""
        begin_time = ""
        try:
            db_begin = str(begin).strip().split(" ")
            begin_date = db_begin[0].split("-")
            print(begin_date)
            begin_last = begin_date[2] + "-" + begin_date[0] + "-" + begin_date[1]

            #begin_date.reverse()
            #print(begin_date)
            #begin_date = "-".join(begin_date)

            begin_date_db = datetime.datetime.strptime(begin_last, "%Y-%m-%d")


            print(begin_date)
            begin_time = db_begin[-1]
            print(begin_time)


        except Exception as e:
            print(e)
            msg = "begin params error!"
            return render_template('add_task.html', current_user=current_user, msg=msg)

        if priority not in ["Higher", "Medium", "Lower"]:
            msg = "priority params error!"
            return render_template('add_task.html', current_user=current_user, msg=msg)
        if name == "":
            msg = "name params error!"
            return render_template('add_task.html', current_user=current_user, msg=msg)

        print(begin_date_db)
        all_task = Task.query.filter_by(user_id=user.id, begin=begin_date_db).all()
        print(all_task)
        print(len(all_task))
        if len(all_task) > 10:
            msg = db_begin[0] + " You have more than 10 tasks！"
            return render_template('add_task.html', current_user=current_user, msg=msg)

        task = Task(name=name.replace("\n", ""), begin=begin_date_db, begin_time=begin_time, user_id=user.id, priority=priority, description=description)
        db.session.add(task)
        db.session.commit()  # 提交事务

        return redirect(url_for('main.index'))


@main.route('/history')
@login_required
def history():
    if request.method == 'GET':
        all_task = Task.query.filter_by(user_id=int(current_user.id)).all()
        print(all_task)
        return render_template('history.html', current_user=current_user, all_task=all_task)


@main.route('/delete_task', methods=['POST'])
def delete_task():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        cid = data['id']

        task = Task.query.get(cid)
        if not task:
            return jsonify({"status": "2", "data": "This task has been deleted"})
        else:
            try:
                db.session.delete(task)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

        return jsonify({"status": "0", "data": "successfully deleted！"})
    else:
        return jsonify({"status": "0", "data": "delete"})

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html', msg="Account password error")

    else:
        return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        if password2 != password:
            return render_template('register.html', msg="Confirm password and password do not match")
        user = User.query.filter_by(username=username).first()
        if user is not None:
            return render_template('register.html', msg="Username already exists")
        else:
            us = User(username=username, password=password)
            db.session.add(us)
            db.session.commit()  # 提交事务
            return redirect(url_for('main.login'))

    else:
        return render_template('register.html')
