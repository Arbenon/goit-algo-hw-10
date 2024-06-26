# goit-algo-hw-10
GOIT homework 10

Вимірювання інтеграла

#
Інтеграл, обчислений методом Монте-Карло: ~2.65567 (точне значення може змінюватися через випадковість)
Аналітично обчислений інтеграл: 2.6667
Інтеграл, обчислений за допомогою функції quad: 2.6667

##
Після виконання обчислень і порівняння результатів можна зробити наступні висновки:

    Метод Монте-Карло є ефективним інструментом для обчислення наближених значень визначених інтегралів, особливо коли аналітичне або чисельне розв'язання важке або неможливе.

    У випадку нашої функції f(x)=x2f(x)=x2, метод Монте-Карло успішно апроксимував значення інтегралу, яке було порівняне з аналітичним розв'язком та результатом, отриманим за допомогою чисельної інтеграції з використанням функції quad з бібліотеки scipy.

    Порівняння результатів показало, що отримане методом Монте-Карло значення інтегралу було досить близьким до аналітичного та чисельного розв'язків, що свідчить про ефективність цього методу для обчислення визначених інтегралів. Точність методу Монте-Карло значно залежить від кількості випадкових точок, які використовуються для оцінки інтегралу. Зазвичай збільшення кількості точок призводить до більш точного результату, однак це може збільшити обчислювальні витрати.

    Метод Монте-Карло є стохастичним, тобто результати можуть змінюватися при кожному запуску програми через випадковий характер генерації випадкових точок. Однак з використанням достатньо великої кількості точок середнє значення буде наближатися до точного значення інтегралу.