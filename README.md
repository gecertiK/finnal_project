# shop/store
Docker, gocker-copose, nginx, postgres, redis, rabbitmq, celery, mailhog.

Склад - admin и api. Кладовщик додлжен иметь возможность через адмику добавлять книги (инстансы книг) и обрабатывать пришедгие заказы. Api - используется магазином что бы создать заказ. Использует первую базу.

Магазин - регистрация, фильтрация книг, заполнение корзины, оформление заказа. Использует вторую базу. Есть кеширование.

Celery - периодически синхронизирует наличие книг из склада в магазин.

Mailhog - получает почту за пользователя о том что заказ оформлен и о том что заказ выполнен.