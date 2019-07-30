<div align="center">
  <a href="https://evaluateprofs.com">
    <img src="https://github.com/simplyalde/evaluateprofs-dev/blob/master/evaluateprofs/static/logo.png">
  </a>
</div>

-----------------

# evaluateprofs.com

Development repository for evaluateprofs.com since original one has some secret data. 

### Prerequisites

To run locally you need following python packages:

```
django    2.2.1
requests  2.22.0
urllib3   1.25.3
```

## Installation

1. Clone the repository.
2. Create *local_settings.py* file and set everything as you want.
3. Change SECRET_KEY and GOOGLE_RECAPTCHA_SECRET_KEY. Fill everything for mailing. Also enter recaptcha keys into *signup.html* and *professor_profile.html* files.
4. Migrate to get the database setted: 

```
python manage.py migrate
```

5. To run the website locally: 

```
python manage.py runserver
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Bootstrap](https://getbootstrap.com/docs/4.3/) - Used for the front-end 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
