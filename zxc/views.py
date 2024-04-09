from django.shortcuts import render
import sqlite3

# Create your views here.

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    c = sqlite3.connect('programm.db')
    cur = c.cursor()
    cur.execute("SELECT Time,Title,Sites from Program_of_the_festival")
    test = cur.fetchall()
    return render(request, '2_page.html', {'test': test})