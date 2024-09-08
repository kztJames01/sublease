/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [
        'puddle/core/templates/core/*.html',
        'puddle/core/static/core/*.css',
        'puddle/item/templates/item/*.html',
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
                'brush': ["Sickness Lines", 'sans-serif'],
            },
            borderWidth: {
                'dotted': '1px',
            },
        },
        plugins: [],
    }
}