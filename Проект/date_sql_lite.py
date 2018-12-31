if len(a[index].date) != 0:
    execute2 = "insert into Olympiad(olymp_id,date_start,date_stop,name) values(?,?,?,?)"
    cursor.execute(execute2, (
    a[index].id,
    a[index].date.get('start')
    a[index].date.get('stop')
    a[index].date.get('name')
    ))
