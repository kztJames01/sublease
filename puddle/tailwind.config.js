/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [
        'shopping_app/core/templates/core/*.html',
        'shopping_app/core/static/core/*.css',
        'shopping_app/core/static/core/*.js',
        'shopping_app/item/templates/item/*.html',
        'shopping_app/Order/static/*.html',
    ],
    theme: {
        extend: {
            fontSize: {
                'xs': '.5rem',
                '5xl': '3rem',
                '6xl': '4rem',
                '7xl': '5rem',
                '8xl': '6rem',
            },

            fontFamily: {
                'robo': ["Roboto Slab", 'serif'],
                'brush': ['Sickness Lines', 'sans-serif'],
            },
            borderWidth: {
                'dotted': '1px',
            },
        },
        plugins: [],
    }
}