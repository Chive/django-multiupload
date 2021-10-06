setup:
	make clean
	mkdir -p testing
	make prep-env envname=py3.9-dj2.2
	make prep-env envname=py3.9-dj3.1
	make prep-env envname=py3.9-dj3.2

start-22:
	make runserver envname=py3.9-dj2.2

start-31:
	make runserver envname=py3.9-dj3.1

start-32:
	make runserver envname=py3.9-dj3.2


prep-env:
	mkdir testing/$(envname)
	.tox/$(envname)/bin/django-admin startproject testproject testing/$(envname)
	.tox/$(envname)/bin/pip install -e .

	ln -s ../../examples/contact_form testing/$(envname)/
	ln -s ../../examples/simple testing/$(envname)/

	gsed -i "40 i 'simple', 'contact_form'," testing/$(envname)/testproject/settings.py
	.tox/$(envname)/bin/python testing/$(envname)/manage.py migrate
	cp examples/testproject/urls.py testing/$(envname)/testproject/

  # not supported in django 2.x
  # DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_EMAIL=admin@example.com .tox/$(envname)/bin/python testing/$(envname)/manage.py createsuperuser --noinput
	echo "from django.contrib import auth; auth.get_user_model().objects.create_superuser('admin', 'admin@example.com', 'admin')" | .tox/$(envname)/bin/python testing/$(envname)/manage.py shell

runserver:
	.tox/$(envname)/bin/python testing/$(envname)/manage.py runserver localhost:8000

clean:
	 rm -rf testing
