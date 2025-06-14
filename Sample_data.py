from db.models import Tag, Category, Dish, TagDish


def new_data():
    Category.create(name='Бульоны')
    Category.create(name='Закуски')
    Category.create(name='Паста')
    Category.create(name='Вторые блюда')
    Category.create(name='Напитки')

    Dish.create(name='Классический Куриный Бульон (Белое мясо)',
                category_id='1',
                ingredients='''Кости и обрезки курицы (грудка, спинки, крылья), белое мясо по желанию для насыщенности.''',
                recipe='''Ароматика: Лук, морковь, сельдерей (стандартный "мирпуа"), петрушка (стебли + немного листьев), лавровый лист, перец горошком.
Время: 2-4 часа.
Особенность: Самый универсальный и легкий бульон. Не требует обжаривания костей.
Применение: Супы (лапша, рисовый), соусы, тушение овощей, ризотто.''')
    Dish.create(name='Наваристый Говяжий Бульон (Коричневый)',
                category_id='1',
                ingredients='Говяжьи кости (мозговые, трубчатые), возможно немного мяса (хвост, голяшка).',
                recipe='''Ключевой шаг: кости запекаются в духовке до темно-золотистого цвета (45-60 мин при 200°C).
Ароматика: Обжаренные до карамелизации лук, морковь, сельдерей. Томатная паста (добавляется к овощам на сковороду на 1-2 мин). Петрушка, тимьян, лавровый лист, перец горошком.
Время: 6-12 часов (чем дольше, тем насыщеннее).
Особенность: Глубокий, темный цвет и насыщенный мясной вкус благодаря реакции Майяра при запекании.
Применение: Консоме, французские луковые супы, гуляши, тушеные блюда, соусы (демиглас).''')
    Dish.create(name='Прозрачный Рыбный Бульон (Фюме)',
                category_id='1',
                ingredients='Кости и головы белой нежирной рыбы (треска, палтус, морской окунь, камбала).',
                recipe='''Избегать жирной и очень костлявой рыбы (скумбрия, сардина, речная).
Ароматика: Лук, лук-порей (белая часть), сельдерей, петрушка (стебли), фенхель (если есть), лавровый лист, перец горошком. Никакой моркови (дает сладость и мутность)!
Время: 20-40 минут. Никогда не кипятить бурно! Только легкое побулькивание. Иначе бульон станет мутным и горьким.
Особенность: Быстрый, легкий, очень ароматный, должен быть кристально прозрачным.
Применение: Уха, рыбные супы (буйабес), соусы к рыбе, ризотто с морепродуктами.''')
    Dish.create(name='Овощной Бульон (Универсальный)',
                category_id='1',
                ingredients='Разнообразные овощи и их обрезки (лук, морковь, сельдерей, лук-порей, грибы, помидоры, капуста белокочанная/савойская, пастернак, петрушка/кинза стебли). Избегать брокколи, цветной капусты, брюссельской капусты, свеклы, картофеля (дают сильный или крахмалистый вкус/мутность).',
                recipe='''Ароматика: Чеснок, лавровый лист, перец горошком, тимьян, розмарин, зира (по желанию). Можно добавить сушеные грибы (шиитаке) для глубины "умами".
Время: 45-60 минут.
Особенность: Веганский/вегетарианский, легкий, зависит от сезона овощей. Не кипятить слишком долго.
Применение: Вегетарианские супы, тушение овощей и круп, приготовление риса/киноа, основа для соусов.''')
    Dish.create(name='Грибной Бульон (Глубокий "Умами")',
                category_id='1',
                ingredients=' Свежие грибы (шампиньоны, вешенки) + обязательно сушеные грибы (белые, подберезовики, шиитаке) и вода от их замачивания. Обрезки грибов.',
                recipe=''' Ароматика: Лук, чеснок, морковь, сельдерей, петрушка стебли, тимьян, лавровый лист, перец горошком. Ключевой шаг: обжарить свежие грибы до золотистого цвета и выпаривания влаги.
Время: 45-60 минут.
Особенность: Интенсивный грибной аромат и вкус "умами", темный цвет. Вода от замачивания сухих грибов – сокровище!
Применение: Грибные супы и соусы, ризотто, тушеные блюда с грибами, вегетарианские подливы.''')
    Dish.create(name='Свиной Бульон (Тонизирующий / Для Рамен)',
                category_id='1',
                ingredients='Свиные кости (ножки, хвосты, ребра, позвоночник)',
                recipe='''Ключевой шаг: Кости обязательно бланшировать 10-15 мин, слить воду, промыть. Это удалит излишки крови и примеси для чистоты бульона. Затем варить, часто с добавлением куриных костей.
Ароматика: Лук, чеснок, имбирь (ломтики), зеленый лук, грибы шиитаке (сушеные или свежие), соевый соус (иногда на последнем этапе), звездочка аниса, корица (палочка), сычуаньский перец (по желанию). Морковь и сельдерей не всегда используются.
Время: 6-12 часов (особенно для бульона Тонкоцу - должен стать молочно-белым).
Особенность: Очень наваристый, часто жирный, с характерным свиным ароматом. Для Тонкоцу требуется интенсивное кипение.
Применение: Бульон для рамен (особенно Тонкоцу), фо бо, тушеные свиные блюда, кислые супы. ''')

    Dish.create(name='Брускетта с Томатами и Базиликом (Итальянская классика)',
                category_id='2',
                ingredients='Багет/чиабатта, спелые помидоры (лучше черри или "бычье сердце"), свежий базилик, чеснок (1-2 зубка), оливковое масло extra virgin, бальзамический крем (опционально), соль, перец.',
                recipe='''Хлеб нарезать ломтиками, обжарить/подсушить в духовке до хруста. Горячий хлеб натереть разрезанным зубчиком чеснока. Помидоры мелко нарезать/кубиком, 
смешать с рубленым базиликом, солью, перцем и оливковым маслом. Выложить смесь на хлеб. Сбрызнуть бальзамиком. Изюминка: Простота и яркость свежих вкусов.''')
    Dish.create(name='Тартар из Говядины (Изысканная сырая закуска)',
                category_id='2',
                ingredients='''Свежайшая говяжья вырезка (200-250 г), красный лук (мелко рубленный), корнишоны (мелко рубленные), каперсы (мелко рубленные), 
желток перепелиного/куриного яйца, дижонская горчица (1 ч.л.), вустерширский соус (несколько капель), табаско (по вкусу), оливковое масло, соль, свежемолотый перец, зелень петрушки/кинзы.''',
                recipe='''Мясо очень острым ножом нарезать мельчайшим кубиком (не прокручивать!). Смешать с луком, корнишонами, каперсами. 
Добавить горчицу, соусы, масло, соль, перец. Аккуратно перемешать. Сформировать шарик или кружок, сделать углубление сверху. 
Перед подачей в углубление аккуратно выложить желток. Украсить зеленью. Подавать с чипсами, гренками или листьями салата. Изюминка: Нежный вкус сырого мяса и смелый вид.''')
    Dish.create(name='Запеченный Камамбер с Орехами и Медом (Плавится на глазах)',
                category_id='2',
                ingredients='''Сыр Камамбер в деревянной коробочке (1 шт.), 
грецкие орехи/пекан (горсть, порубить), жидкий мед (2-3 ст.л.), свежий тимьян/розмарин (несколько веточек), свежемолотый перец, багет для подачи.''',
                recipe='''Сыр достать из коробки, снять верхнюю корку (или сделать крестообразный надрез). Положить обратно в коробку (или на пергамент/в форму). Посыпать орехами, полить медом, украсить веточками травы, поперчить. 
Запекать в разогретой до 180°C духовке 10-15 минут, пока сыр не станет очень мягким внутри. Подавать немедленно с нарезанным багетом. Изюминка: Театральная подача и сочетание соленого, сладкого и орехового.''')
    Dish.create(name='Цукини Фри с Соусом Ремулад (Легкая и хрустящая)',
                category_id='2',
                ingredients='''Молодые цукини (2-3 шт.), панировочные сухари (лучше панко), тертый пармезан (2-3 ст.л.), яйцо (1 шт.), мука, чесночный порошок, паприка, соль, перец, оливковое масло/масло для фритюра.
Для Ремулада: Майонез (3 ст.л.), мелкорубленные корнишоны (1 ст.л.), каперсы (1 ч.л.), зелень петрушки/укропа, лимонный сок (1 ч.л.), дижонская горчица (1/2 ч.л.), соль, перец.''',
                recipe='''Цукини нарезать брусочками. Обвалять в муке, затем во взбитом яйце, затем в смеси сухарей панко, пармезана, специй. Обжарить во фритюре или запечь в духовке (200°C, 15-20 мин) до золотистости. 
Для ремулада смешать все ингредиенты. Подавать цукини горячими с соусом. Изюминка: Альтернатива картофелю фри, более легкая и сочная.''')
    Dish.create(name='Мини-Самосы с Картофелем и Горошком (Индийский стиль)',
                category_id='2',
                ingredients='''Готовое слоеное тесто/тесто фило/пельменное тесто (упрощает процесс), картофель (отварной и размятый), 
зеленый горошек (свежий/замороженный, бланшированный), лук (мелко рубленный, обжаренный), свежий имбирь (тертый), зира, куркума, кориандр молотый, острый перец чили (по вкусу), зелень кинзы, соль, масло для жарки.''',
                recipe='''Смешать начинку: картофель, горошек, лук, специи, зелень. Тесто раскатать, нарезать на квадратики/полоски. Выложить начинку, сформировать треугольники (самосы). Обжарить во фритюре до золотистости или запечь в духовке (смазать маслом). 
Подавать с мятным или тамариндовым чатни. Изюминка: Хрустящие, ароматные, с пикантной начинкой.''')
    Dish.create(name='Фаршированные Мини-Перцы с Козьим Сыром (Цветасто и вкусно)',
                category_id='2',
                ingredients='''Мини-перцы разных цветов (10-15 шт.), козий сыр (мягкий, 100-150 г), сливочный сыр/рикотта (50 г), мед (1 ч.л.), 
лимонная цедра, свежий тимьян/розмарин (рубленный), грецкие орехи/фисташки (порубить), соль, перец.''',
                recipe='''Перцы разрезать вдоль пополам, удалить семена. Смешать козий сыр, сливочный сыр, мед, цедру, травы, соль, перец до однородности. Начинить половинки перцев сырной смесью. Посыпать орехами. Запекать 10-12 минут при 180°C или подавать холодными. 
Изюминка: Яркие цвета, контраст нежного сыра и хрустящего перца, сладко-соленый вкус.''')

    Dish.create(name='Спагетти Карбонара (Классика Рима)',
                category_id='3',
                ingredients='''Спагетти - 200 г
Гуанчиале или Панчетта (кубиками) - 100 г (или качественный бекон)
Пекорино Романо (тертый) - 50 г
Пармиджано Реджано (тертый) - 25 г
Яичные желтки - 3 крупных (или 2 целых яйца + 1 желток)
Свежемолотый черный перец - обильно
Соль - по вкусу''',
                recipe='''Готовим мясо: На сухой сковороде обжарьте гуанчиале/панчетту на среднем огне до хрустящей корочки и вытопленного жира. Снимите с огня. Не сливайте жир!
Готовим пасту: В кипящей подсоленной воде отварите спагетти до состояния "аль денте" (чуть твердые внутри). Сохраните 1 стакан крахмальной воды!
Делаем соус: В миске взбейте желтки (или яйца с желтком) с большим количеством свежемолотого черного перца и большей частью тертого сыра (пекорино + пармезан).
Соединяем: Слейте пасту, оставив немного воды. НЕМЕДЛЕННО переложите горячие спагетти в сковороду с мясом и жиром. Снимите с огня (важно, чтобы сковорода не была слишком горячей, иначе яйца свернутся!). Быстро перемешайте.
Эмульгируем: Влейте яично-сырную смесь к пасте. Энергично перемешивайте, добавляя понемногу сохраненную крахмальную воду (2-4 ст.л.), пока не получится кремовый, нежный соус, обволакивающий пасту. Соус должен быть гладким, а не превратиться в яичницу.
Подаем: Немедленно разложите по тарелкам, щедро посыпьте оставшимся сыром и свежемолотым черным перцем.''')
    Dish.create(name='Пенне алла Водка (Кремовый томатно-сливочный)',
                category_id='3',
                ingredients='''Пенне - 200 г
Оливковое масло - 2 ст.л.
Лук (мелко руб.) - 1/2 шт.
Чеснок (давленый) - 2 зубка
Томатная паста - 2 ст.л.
Водка - 1/4 ст. (60 мл)
Помидоры в собственном соку (измельченные) - 400 г
Сливки 20-33% - 1/2 ст. (120 мл)
Соль, перец чили хлопьями - по вкусу
Сахар (опционально) - щепотка
Базилик свежий (рубленый) - для подачи
Пармезан (тертый) - для подачи''',
                recipe='''Паста: Отварите пенне в подсоленной воде до "аль денте". Сохраните 1 стакан воды.
Соус: В глубокой сковороде разогрейте масло. Обжарьте лук до прозрачности (5 мин). Добавьте чеснок и хлопья чили, жарьте 1 мин до аромата.
Томатная паста: Добавьте томатную пасту. Жарьте, помешивая, 2-3 минуты, пока она не потемнеет и не станет ароматной.
Водка: Влейте водку. Увеличьте огонь и варите, помешивая, 2-3 минуты, чтобы алкоголь выпарился.
Помидоры: Добавьте измельченные помидоры, соль, перец, сахар (если помидоры кислые). Доведите до кипения, убавьте огонь и тушите 10-15 минут, пока соус немного загустеет.
Сливки и паста: Влейте сливки, прогрейте 2 минуты. Добавьте отваренные пенне и немного крахмальной воды. Хорошо перемешайте, чтобы паста покрылась соусом. Готовьте 1-2 мин.
Подаем: Посыпьте рубленым базиликом и тертым пармезаном.''')
    Dish.create(name='Феттучине Альфредо (Роскошный сливочный)',
                category_id='3',
                ingredients='''Феттучине - 200 г
Сливочное масло (качественное) - 100 г
Сливки 33% - 150 мл
Пармиджано Реджано (свежетертый) - 100 г + еще для подачи
Мускатный орех (свежетертый) - щепотка
Соль, свежемолотый белый перец - по вкусу''',
                recipe='''Паста: Отварите феттучине в подсоленной воде до "аль денте". Сохраните 1 стакан воды. Не промывайте!
Соус: В большой сковороде на слабом огне растопите сливочное масло. Влейте сливки, добавьте щепотку соли, белый перец и мускатный орех. Прогрейте, не доводя до кипения.
Соединение: Добавьте большую часть тертого пармезана в соус, перемешайте до легкого загустения. Слейте пасту, дайте стечь воде. Переложите горячие феттучине сразу в сковороду с соусом.
Эмульгирование: Снимите с огня. Энергично перемешивайте пасту с соусом, добавляя понемногу крахмальной воды (2-4 ст.л.), пока не получится гладкий, шелковистый, кремовый соус, обволакивающий ленточки пасты.
Подаем: Немедленно разложите по подогретым тарелкам, обильно посыпьте оставшимся пармезаном и свежемолотым белым перцем.''')
    Dish.create(name='Лингвини с Морепродуктами (Делия)',
                category_id='3',
                ingredients='''Лингвини - 200 г
Смесь морепродуктов (креветки очищ., мидии, кальмары кольца) - 300 г
Оливковое масло - 3 ст.л.
Чеснок (давленый) - 3 зубка
Перец чили (сушеный, хлопья или свежий мелко руб.) - по вкусу
Белое сухое вино - 1/2 ст. (120 мл)
Помидоры черри (половинки) - 150 г
Петрушка свежая (рубленая) - горсть
Соль, свежемолотый черный перец
Лимонная цедра - 1 ч.л.''',
                recipe='''Паста: Отварите лингвини до "аль денте". Сохраните 1 стакан воды.
Морепродукты: Разогрейте масло в большой сковороде на среднем огне. Обжарьте чеснок и чили 1 мин до аромата (не давайте чесноку подгореть!).
Обжарка: Добавьте морепродукты (если креветки крупные, их сначала, затем кальмары, мидии в конце). Обжаривайте 2-3 минуты, пока креветки не порозовеют, а кальмары не побелеют.
Вино и томаты: Влейте вино, увеличьте огонь и дайте покипеть 1-2 мин, чтобы алкоголь выпарился. Добавьте помидоры черри, соль, перец. Тушите 2-3 мин.
Соединение: Добавьте отваренные лингвини в сковороду. Влейте немного крахмальной воды. Аккуратно перемешайте, чтобы паста пропиталась соусом и морепродукты распределились. Готовьте 1-2 мин.
Подаем: Снимите с огня, добавьте петрушку и лимонную цедру. Перемешайте и подавайте немедленно.''')
    Dish.create(name='Ореккьете с Брокколи и Анчоусами (Пулийский)',
                category_id='3',
                ingredients='''Ореккьете - 200 г
Брокколи (соцветия) - 1 средний кочан (около 300г)
Оливковое масло - 4 ст.л.
Чеснок (давленый) - 2-3 зубка
Анчоусы в масле (филе, рубленые) - 4-6 шт.
Перец чили хлопьями - щепотка
Панировочные сухари (Панко или обычные) - 3 ст.л.
Соль, свежемолотый черный перец''',
                recipe='''Паста: Отварите ореккьете в подсоленной воде до "аль денте". За 3 минуты до готовности добавьте соцветия брокколи в кастрюлю. Сохраните 1 стакан воды. Слейте пасту и брокколи.
Обжарка анчоусов: В большой сковороде разогрейте 3 ст.л. оливкового масла. Обжарьте чеснок и чили 30 сек. Добавьте рубленые анчоусы. Жарьте, помешивая, пока анчоусы не "растворятся" (1-2 мин).
Гренки (Пангратта): В отдельной маленькой сковороде разогрейте 1 ст.л. оливкового масла. Обжарьте панировочные сухари до золотистого цвета и хруста. Снимите с огня.
Соединение: Добавьте пасту и брокколи в сковороду с анчоусами. Влейте немного крахмальной воды. Аккуратно перемешайте на среднем огне, чтобы все покрылось маслом и ароматами (1-2 мин). Приправьте перцем (солить осторожно, анчоусы соленые!).
Подаем: Разложите по тарелкам, щедро посыпьте хрустящими гренками (панграттой).''')
    Dish.create(name='Паста алла Норма (Сицилийский)',
                category_id='3',
                ingredients='''Паста - 200 г
Баклажаны - 1-2 крупных (около 400г)
Оливковое масло - для жарки + 2 ст.л.
Лук (мелко руб.) - 1/2 шт.
Чеснок (давленый) - 1 зубок
Помидоры в собственном соку (измельченные) - 400 г
Базилик свежий (листья) - горсть + для подачи
Рикотта салата (или солена) - 150 г
Соль''',
                recipe='''Баклажаны: Баклажаны нарежьте кубиками 1.5-2 см. Посолите, оставьте на 20-30 мин. Промойте и хорошо обсушите. Обжарьте порциями в большом количестве разогретого оливкового масла до золотистого цвета и мягкости внутри. Выложите на бумажные полотенца.
Соус: В другой сковороде разогрейте 2 ст.л. масла. Обжарьте лук до мягкости (5-7 мин). Добавьте чеснок, жарьте 1 мин. Влейте помидоры, добавьте несколько листьев базилика, соль. Доведите до кипения, убавьте огонь и тушите 15-20 мин, пока соус не загустеет.
Паста: Отварите пасту до "аль денте". Сохраните 1 стакан воды.
Соединение: Добавьте обжаренные баклажаны в томатный соус, прогрейте 2 мин. Добавьте отварную пасту, немного крахмальной воды. Аккуратно перемешайте.
Подаем: Разложите по тарелкам. Сверху выложите ложки рикотты (соленой или салаты), посыпьте свежим базиликом.''')

    Dish.create(name='Запеченная Куриная Грудка в Сметанно-Чесночном Соусе',
                category_id='4',
                ingredients='''Куриное филе (грудка) - 2 шт. (около 300-400 г)
Сметана (15-20%) - 150 г
Чеснок - 3-4 зубка (давленый)
Горчица дижонская - 1 ст.л.
Лимонный сок - 1 ст.л.
Соль, свежемолотый черный перец - по вкусу
Паприка сладкая (копченая или обычная) - 1 ч.л.
Свежие травы (петрушка, укроп) - для подачи
Растительное масло - 1 ст.л. (для смазки формы)''',
                recipe='''Маринад: В миске смешайте сметану, давленый чеснок, дижонскую горчицу, лимонный сок, паприку, соль и перец.
Курица: Филе слегка отбейте, если толстое. Обсушите бумажным полотенцем. Посолите и поперчите.
Замариновать: Обмажьте куриные грудки соусом со всех сторон. Оставьте мариноваться минимум на 20-30 минут (можно до 2 часов в холодильнике).
Запекание: Разогрейте духовку до 200°C. Смажьте форму для запекания маслом. Выложите курицу. Запекайте 20-25 минут до готовности (внутренняя температура 74°C) и легкой румяности. Если соус начинает подгорать, накройте фольгой.
Подача: Подавайте горячими, полив соусом из формы и посыпав свежей зеленью. Гарнир: картофельное пюре, рис, тушеные овощи.''')
    Dish.create(name='Говяжий Строганов (Бефстроганов)',
                category_id='4',
                ingredients='''Говяжья вырезка (или филе) - 300 г (нарезать тонкими брусочками поперек волокон)
Шампиньоны - 200 г (нарезать пластинками)
Лук репчатый - 1 шт. (средний, тонко нарезать полукольцами/кубиками)
Сливочное масло - 2 ст.л.
Растительное масло - 1 ст.л.
Мука пшеничная - 1 ст.л.
Говяжий бульон - 150-200 мл (или вода + кубик бульона)
Сметана (20%) - 100-150 г
Томатная паста - 1 ч.л. (опционально)
Дижонская горчица - 1 ч.л. (опционально)
Соль, свежемолотый черный перец - по вкусу
Петрушка свежая - для подачи''',
                recipe='''Мясо: Обсушите мясо бумажным полотенцем. Посолите и поперчите.
Обжарка мяса: В сковороде или сотейнике разогрейте 1 ст.л. сливочного и 1 ст.л. растительного масла на сильном огне. Быстро обжарьте мясо порциями до легкой корочки (не пережаривать, 1-2 мин на порцию). Выньте.
Лук и грибы: В той же сковороде растопите оставшееся сливочное масло. Обжарьте лук до мягкости (5 мин). Добавьте грибы, жарьте до золотистого цвета и выпаривания жидкости (8-10 мин).
Соус: Посыпьте лук и грибы мукой, перемешайте, жарьте 1 мин. Постепенно влейте бульон, помешивая венчиком, чтобы не было комков. Доведите до кипения. Добавьте томатную пасту и горчицу (если используете), перемешайте.
Тушение: Верните мясо в сковороду вместе с выделившимся соком. Убавьте огонь до минимума, тушите под крышкой 10-15 минут, пока мясо не станет мягким.
Сметана: Снимите с огня, добавьте сметану. Аккуратно перемешайте, прогрейте, НЕ ДОВОДЯ ДО КИПЕНИЯ (иначе сметана свернется). Попробуйте, при необходимости посолите/поперчите.
Подача: Подавайте горячим, посыпав петрушкой. Традиционный гарнир: картофельное пюре, рис или гречневая каша.''')
    Dish.create(name='Лосось на Подушке из Овощей, Запеченный в Духовке',
                category_id='4',
                ingredients='''Филе лосося (с кожей или без) - 2 порции (около 300 г)
Кабачок (цуккини) - 1 небольшой (нарезать полукружками)
Помидоры черри - 150 г (разрезать пополам)
Лук красный - 1/2 шт. (тонкие полукольца)
Лимон - 1/2 шт. (ломтики + сок)
Оливковое масло - 2 ст.л.
Соль, свежемолотый черный перец - по вкусу
Сушеные травы (прованские, итальянские) - 1 ч.л.
Чеснок - 1-2 зубка (давленый, опционально)''',
                recipe='''Овощи: Разогрейте духовку до 200°C. В форму для запекания выложите кабачок, черри и лук. Сбрызните 1 ст.л. оливкового масла, посолите, поперчите, посыпьте травами и чесноком (если используете). Перемешайте.
Запекание овощей: Запекайте 15 минут.
Рыба: Лосось обсушите, сбрызните лимонным соком, посолите, поперчите. Смажьте оставшимся маслом.
Запекание с рыбой: Достаньте форму, перемешайте овощи. Сверху на овощи положите филе лосося кожей вниз (если есть кожа). Разложите ломтики лимона поверх рыбы.
Готовка: Верните форму в духовку. Запекайте еще 10-15 минут (время зависит от толщины филе) до желаемой степени прожарки (рыба должна легко расслаиваться вилкой).
Подача: Подавайте горячим прямо в форме или аккуратно переложив на тарелки с овощами. Гарнир: можно добавить отварной молодой картофель или зеленый салат.''')
    Dish.create(name='Свиные Медальоны в Яблочно-Горчичном Соусе',
                category_id='4',
                ingredients='''Свиная вырезка - 300-400 г (нарезать поперек волокон на медальоны толщиной 2-2.5 см)
Растительное масло - 2 ст.л.
Сливочное масло - 1 ст.л.
Яблоко (твердый сорт) - 1 большое (очистить, удалить сердцевину, нарезать дольками)
Лук репчатый - 1/2 шт. (тонко нарезать)
Чеснок - 1 зубок (давленый)
Яблочный сок или сидр - 100 мл
Куриный/овощной бульон - 100 мл
Дижонская горчица - 1 ст.л. (или зернистая)
Сливки 10-20% - 50 мл (опционально, для кремовости)
Соль, свежемолотый черный перец - по вкусу
Свежий тимьян/розмарин - несколько веточек''',
                recipe='''Медальоны: Обсушите медальоны бумажным полотенцем. Посолите и поперчите с обеих сторон.
Обжарка: Разогрейте в сковороде растительное масло на сильном огне. Обжарьте медальоны по 1.5-2 минуты с каждой стороны до золотистой корочки. Выньте.
Овощи/Фрукты: В той же сковороде добавьте сливочное масло. Обжарьте лук до мягкости (3-4 мин). Добавьте яблоки, жарьте 3-4 минуты до легкой карамелизации. Добавьте чеснок и тимьян/розмарин, жарьте 30 сек.
Соус: Влейте яблочный сок/сидр, соскребите лопаткой прижаренные кусочки со дна. Доведите до кипения, уварите наполовину (1-2 мин). Влейте бульон, доведите до кипения. Убавьте огонь.
Тушение: Верните медальоны в сковороду. Тушите под крышкой на медленном огне 8-12 минут до готовности свинины (внутр. темп. 63°C).
Завершение соуса: Выньте медальоны. Добавьте в соус горчицу и сливки (если используете). Прогрейте, помешивая, 1-2 мин (не кипятить!). Попробуйте, посолите/поперчите при необходимости. Удалите веточки трав.
Подача: Подавайте медальоны, полив горячим соусом с яблоками. Гарнир: картофельное пюре, рис или тушеная капуста.''')
    Dish.create(name='Котлеты из Нута и Овощей (Веганские)',
                category_id='4',
                ingredients='''Нут консервированный - 1 банка (240г нетто, промыть, обсушить)
Морковь - 1 шт. (мелко натереть)
Лук репчатый - 1/2 шт. (мелко нарезать)
Чеснок - 2 зубка (давленый)
Зелень (петрушка, кинза) - горсть (рубленая)
Овсяные хлопья быстрого приготовления - 4-5 ст.л. (или панировочные сухари)
Мука нутовая/пшеничная - 1-2 ст.л. (для связи)
Лимонный сок - 1 ст.л.
Зира (кумин), кориандр молотый, паприка - по 1/2 ч.л.
Соль, свежемолотый черный перец - по вкусу
Растительное масло - для жарки''',
                recipe='''Пюре: Частью нута размажьте вилкой или измельчите в блендере в грубое пюре.
Смесь: В миске смешайте нутовое пюре, цельный нут, тертую морковь, лук, чеснок, зелень, специи, лимонный сок, соль, перец.
Связка: Добавьте овсяные хлопья и 1 ст.л. муки. Тщательно перемешайте. Масса должна держать форму. Если слишком влажно, добавьте еще муки/хлопьев. Если сухо - немного воды. Дайте постоять 5-10 мин.
Формовка: Сформируйте котлеты.
Жарка: Разогрейте масло в сковороде на среднем огне. Обжарьте котлеты с двух сторон до золотистой корочки (по 3-4 мин с каждой стороны). Можно запечь в духовке (200°C, 15-20 мин, смазав маслом).
Подача: Подавайте с йогуртовым/чесночным соусом, хумусом, свежими овощами, в пите или с салатом.''')
    Dish.create(name='Тушеная Говядина с Черносливом (по-Домашнему)',
                category_id='4',
                ingredients='''Говядина (огузок, лопатка, щека) - 500 г (нарезать крупными кубиками 3-4 см)
Лук репчатый - 2 шт. (крупно нарезать)
Морковь - 2 шт. (крупно нарезать)
Чернослив без косточек - 100-150 г
Томатная паста - 1 ст.л.
Мука пшеничная - 1 ст.л. (для мяса)
Растительное масло - 2 ст.л.
Говяжий бульон/вода - 400-500 мл
Лавровый лист - 1-2 шт.
Душистый перец горошком - 3-4 шт.
Соль, свежемолотый черный перец - по вкусу
Сахар - щепотка (опционально)''',
                recipe='''Мясо: Обсушите мясо. Обваляйте в муке, стряхните излишки.
Обжарка мяса: Разогрейте масло в кастрюле/сотейнике с толстым дном на сильном огне. Обжарьте мясо порциями до румяной корочки со всех сторон. Выньте.
Овощи: В той же посуде обжарьте лук и морковь 5-7 минут до мягкости. Добавьте томатную пасту, жарьте 1-2 мин.
Тушение: Верните мясо. Добавьте чернослив, лавровый лист, перец горошком. Залейте горячим бульоном/водой так, чтобы жидкость почти покрывала мясо. Доведите до кипения. Убавьте огонь до минимального. Накройте крышкой.
Готовка: Тушите 1.5 - 2 часа, пока мясо не станет очень мягким (проверяйте вилкой). За 20 минут до конца посолите, поперчите, добавьте щепотку сахара, если нужно. При необходимости добавьте немного кипятка.
Подача: Подавайте горячим, удалив лавровый лист и перец горошком. Отличный гарнир: картофельное пюре, гречка, макароны.''')

    Dish.create(name='Домашний Лимонад с Мятой и Имбирем',
                category_id='5',
                ingredients='''4 лимона (сок)
1 л холодной воды
4 ст. л. сахара (или мёда)
1 небольшой корень имбиря (2-3 см, тонко нарезать)
Горсть свежей мяты
Лёд''',
                recipe='''В кувшин выдавите лимонный сок, добавьте сахар (или мёд) и перемешайте до растворения.
Добавьте нарезанный имбирь и мяту.
Залейте холодной водой, дайте настояться 10-15 минут.
Подавайте со льдом.''')
    Dish.create(name='Молочный Коктейль с Орео',
                category_id='5',
                ingredients='''300 мл молока
100 мл ванильного мороженого
5 печений Oreo
Взбитые сливки (по желанию)''',
                recipe='''В блендер положите печенье, молоко и мороженое.
Взбейте до однородности.
Разлейте по бокалам, украсьте взбитыми сливками и крошкой Oreo.''')
    Dish.create(name='Мохито Безалкогольный',
                category_id='5',
                ingredients='''1 лайм (нарезать дольками)
10 листиков мяты
2 ч. л. сахара
200 мл газированной воды
Лёд''',
                recipe='''В стакан положите мяту, лайм и сахар. Разомните ложкой.
Добавьте лёд, залейте газировкой.
Аккуратно перемешайте.''')
    Dish.create(name='Глинтвейн (Безалкогольный)',
                category_id='5',
                ingredients='''1 л виноградного сока
1 апельсин (дольки)
1 палочка корицы
3-4 гвоздики
2 звездочки бадьяна
1 ч. л. мёда''',
                recipe='''В кастрюлю налейте сок, добавьте специи и апельсин.
Нагревайте на слабом огне 10-15 минут (не кипятить!).
Процедите, добавьте мёд. Подавайте тёплым.''')
    Dish.create(name='Клубничный Смузи',
                category_id='5',
                ingredients='''200 г клубники (свежей или замороженной)
1 банан
150 мл йогурта (или молока)
1 ч. л. мёда
Лёд (по желанию)''',
                recipe='''В блендер положите все ингредиенты.
Взбейте до однородности.
Подавайте охлаждённым.''')
    Dish.create(name='Морс из Клюквы',
                category_id='5',
                ingredients='''200 г клюквы (свежей или замороженной)
1 л воды
4-5 ст. л. сахара (по вкусу)
Лимонная цедра (по желанию)''',
                recipe='''Разомните клюкву, залейте кипятком.
Добавьте сахар, дайте настояться 30 минут.
Процедите, охладите. Подавайте со льдом.''')

    Tag.create(name='Свинина',)
    Tag.create(name='Говядина',)
    Tag.create(name='Рыба', )
    Tag.create(name='Без мяса',)
    Tag.create(name='Грибы',)
    Tag.create(name='Овощи',)
    Tag.create(name='Горячее',)
    Tag.create(name='Холодное',)

    TagDish.create(dish_id='6', tag_id='1')
    TagDish.create(dish_id='13', tag_id='1')
    TagDish.create(dish_id='22', tag_id='1')
    TagDish.create(dish_id='6', tag_id='1')
    TagDish.create(dish_id='2', tag_id='2')
    TagDish.create(dish_id='8', tag_id='2')
    TagDish.create(dish_id='20', tag_id='2')
    TagDish.create(dish_id='24', tag_id='2')
    TagDish.create(dish_id='3', tag_id='3')
    TagDish.create(dish_id='16', tag_id='3')
    TagDish.create(dish_id='21', tag_id='3')
    TagDish.create(dish_id='17', tag_id='3')
    TagDish.create(dish_id='4', tag_id='4')
    TagDish.create(dish_id='7', tag_id='4')
    TagDish.create(dish_id='9', tag_id='4')
    TagDish.create(dish_id='10', tag_id='4')
    TagDish.create(dish_id='12', tag_id='4')
    TagDish.create(dish_id='23', tag_id='4')
    TagDish.create(dish_id='5', tag_id='5')
    TagDish.create(dish_id='14', tag_id='5')
    TagDish.create(dish_id='18', tag_id='5')
    TagDish.create(dish_id='4', tag_id='6')
    TagDish.create(dish_id='7', tag_id='6')
    TagDish.create(dish_id='10', tag_id='6')
    TagDish.create(dish_id='11', tag_id='6')
    TagDish.create(dish_id='12', tag_id='6')
    TagDish.create(dish_id='15', tag_id='6')
    TagDish.create(dish_id='17', tag_id='6')
    TagDish.create(dish_id='19', tag_id='6')
    TagDish.create(dish_id='21', tag_id='6')
    TagDish.create(dish_id='23', tag_id='6')
    TagDish.create(dish_id='1', tag_id='7')
    TagDish.create(dish_id='2', tag_id='7')
    TagDish.create(dish_id='3', tag_id='7')
    TagDish.create(dish_id='4', tag_id='7')
    TagDish.create(dish_id='5', tag_id='7')
    TagDish.create(dish_id='6', tag_id='7')
    TagDish.create(dish_id='13', tag_id='7')
    TagDish.create(dish_id='14', tag_id='7')
    TagDish.create(dish_id='15', tag_id='7')
    TagDish.create(dish_id='16', tag_id='7')
    TagDish.create(dish_id='17', tag_id='7')
    TagDish.create(dish_id='18', tag_id='7')
    TagDish.create(dish_id='28', tag_id='7')
    TagDish.create(dish_id='30', tag_id='7')
    TagDish.create(dish_id='8', tag_id='8')
    TagDish.create(dish_id='25', tag_id='8')
    TagDish.create(dish_id='26', tag_id='8')
    TagDish.create(dish_id='27', tag_id='8')
    TagDish.create(dish_id='29', tag_id='8')
