const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const body = document.body;

const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.setAttribute('data-theme', savedTheme);
} else {
    body.setAttribute('data-theme', 'light');
}

themeToggleBtn.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);

    themeIcon.textContent = newTheme === 'light' ? '🌞' : '🌜';
});

if (savedTheme === 'dark') {
    themeIcon.textContent = '🌜';
} else {
    themeIcon.textContent = '🌞';
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');

    buttons.forEach(button => {
        let isMouseDown = false;

        // Когда кнопка зажата
        button.addEventListener('mousedown', () => {
            isMouseDown = true;
            button.classList.add('active');
        });

        // Когда кнопка отпущена
        document.addEventListener('mouseup', (event) => {
            if (isMouseDown) {
                // Проверяем, находится ли курсор внутри кнопки
                const isCursorInside = button.contains(event.target);

                // Если курсор за пределами кнопки, сбрасываем стили
                if (!isCursorInside) {
                    button.classList.remove('active');
                }

                isMouseDown = false;
            }
        });

        // Когда курсор покидает кнопку
        button.addEventListener('mouseleave', () => {
            if (isMouseDown) {
                button.classList.add('active-outside');
            }
        });

        // Когда курсор возвращается на кнопку
        button.addEventListener('mouseenter', () => {
            if (isMouseDown) {
                button.classList.remove('active-outside');
            }
        });
    });
});