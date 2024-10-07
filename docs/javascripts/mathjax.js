window.MathJax = {
    loader: {load: ['[tex]/physics', '[tex]/gensymb']},
    tex: {
        inlineMath: [["\\(", "\\)"], ["\\$", "\\$"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true,
        packages: {'[+]': ['physics', 'gensymb']}
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
})