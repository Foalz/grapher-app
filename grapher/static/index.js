const data = document.currentScript.dataset;
const points = data.points;
const MQ = MathQuill;

Bokeh.embed.embed_item(JSON.parse(points))
let answerSpan = document.getElementById('answer');
let answerMathField = MQ.MathField(answerSpan);
