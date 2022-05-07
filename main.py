from flask import Flask

app = Flask(__name__)


@app.route('/project_flick', methods=['GET'])
def project():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Проект Заурбека</title>
</head>
<body>
<header>
    <h6><a name="head"></a>Привет;) Ты попал на мой веб сайт</h6>
    </header>
<nav><ul>
    <li><a href="#цели">цели</a></li>
    <li><a href="#cursi">Курс по HTML</a></li>
    <li><a href="#pit">Самый низ сайта</a></li>
</ul>
<ol>
<li><a href="#sp1">Упорядоченные и неупоряноченный списки</a></li>
<li><a href="#sp2">Списки описаний</a></li>
<li><a href="#br">Преформатированный текст и переносы</a></li>
<li><a href="#href">Виды ссылок</a></li>
<li><a href="img">Картинки</a></li>
</nav>
<h4><a name="цели"></a>Цели проекта</h4>
<ol>
    <li><a name="cursi"></a>показать разнообразные фишки в
        HTML.(Подробнее в <a href="https://htmlacademy.ru/study">HTML курсах</a>)</li>
    <li>Заинтересовать вас)</li>
    <li>Выполнить предыдущие пункты</li>
</ol>
<article>
<div>Итак, давайте начинать!
    <p>У нас есть такой замечательный блок как <a href="#head">&lt;header&gt;</a>.
        Это так называемая шапка нашего сайта.</p>
    <p>Если есть шапка, то должен быть и низ сайта <a href="#pit">&lt;footer&gt;</a>.</p>
        <p>Есть главное правило!
        В большенстве таких блоков долна быть замыкающая часть!</p>
        пример:
    <br>&lt;footer&gt;
    <br>&lt;/footer&gt;
    <p><a name="sp1"></a>Есть 2 вида списков:</p>
    <ul>
        <li>Не упорядоченный</li>
        <li>&lt;ul&gt;</li>
        <li>разделитель элементов - &lt;li&gt;</li>
    </ul>
    <ol>
        <li>упорядоченный</li>
        <li>&lt;ol&gt;</li>
        <li>разделитель элементов тоже &lt;li&gt;</li>
        <li>дополнительные расширения найдёте в <a href="#docx">вордовском файле</a></li>
    </ol>
    <h2><a name="sp2"></a>Список описаний</h2>
    <dl>
<dt>&lt;dl&gt;</dt>
        <dd>огранечитель списка</dd>
        <dt>&lt;dt&gt;</dt>
        <dd>Выделение фразы</dd>
        <dt>&lt;dd&gt;</dt>
        <dd>подписи под фразой</dd>
    </dl>
    <p>есть выделение цитаты с помощью <q>&lt;q&gt;</q></p><a name="br"></a>
    <h3>Преформатированный текст</h3>
    <p>выполняется с помощью &lt;pre&gt;</p>
    <pre>Пример
        преформатированного
        текста     с сохранёнными пробелами
                     и переносами строк</pre>

<p>существует также ручной
    <br>перенос
    <br>строк</p>
    <p>&lt;br&gt;</p>
    <p>В данном случае не нужен замыкающий блок;)</p>
</div>
</article>
<article>
    <div>
        <p>можно подключить ссылку с помощью &lt;a&gt;</p><a name="href"></a>
        <p>пример: <q>&lt;a href="ссылка"&gt;<cite>фраза</cite>&lt;/a&gt;</q></p>
        <p><a href="https://colorscheme.ru/html-colors.html">Цвета для css файла в web</a></p>
        <p>можно также <a href="static/teamplates/dop.html">переключиться</a> на другой файл html</p>
        <p>можно <del>зачёркивать</del> слова с помощью &lt;del&gt;
        или же <ins>подчёркивать</ins> с помощью &lt;ins&gt;</p>
        <p>можно делать ссылки-якоря(&lt;a href="#имя"&gt;)
        Имя нужно поставить на место на странице, куда вы хотите с помощью
        нажатия переместиться(&lt;a name="имя"&gt;)</p>
        <p># Обязателен!!!!</p>
    </div>
</article>
<article>
    <div><a name="img"></a>Посленее, что мы будем проходить - <a href="static/teamplates/img.html">
    <ins>ИЗОБРАЖЕНИЯ</ins></a></div>
</article>
<footer>
    <h3><a name="docx" href="HTML_and_CSS.docx" download>более подробная информация об HTML(конспект)</a></h3>
    <h6><a name="pit"></a>Если ты долистал до этого момента, значит тебе было интересно, спасибо)</h6>
</footer>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8081, host='localhost')
