from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to Task management app!")

def contact(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Card</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f3f3f3;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .card {
      background: #fff;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
      width: 250px;
    }
    .card img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      object-fit: cover;
      margin-bottom: 10px;
    }
    .card h2 {
      margin: 8px 0 5px;
      font-size: 20px;
    }
    .card p {
      margin: 3px 0;
      color: #555;
      font-size: 14px;
    }
    .card a {
      display: inline-block;
      margin-top: 10px;
      text-decoration: none;
      color: white;
      background: #0078ff;
      padding: 8px 14px;
      border-radius: 6px;
    }
    .card a:hover {
      background: #005fcc;
    }
  </style>
</head>
<body>
  <div class="card">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREl6x-BJrwrtuFQU25k3cRA5QXd9rE_555WKkvUz_w_1iGZWbmC6acaR6if6KKurM51L8&usqp=CAU" alt="Profile Photo">
    <h2>Mahadi Hasan</h2>
    <p>Software Engineer</p>
    <p>Email: mahadi@example.com</p>
    <a href="mailto:mahadi@example.com">Contact</a>
  </div>
</body>
</html>
''')