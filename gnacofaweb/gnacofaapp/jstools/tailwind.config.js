module.exports = {
    future: {
        removeDeprecatedGapUtilities: false,
        purgeLayersByDefault: true,
    },
    purge: {
        enabled: true, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [
        require("@tailwindcss/forms")({
            strategy: 'base', // only generate global styles
            strategy: 'class', // only generate classes
  }),
    ],
}