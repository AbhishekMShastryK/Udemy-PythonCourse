from flask import Flask,render_template

app = Flask(__name__)

@app.route('/plot/')

def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start_time = datetime.datetime(2020,1,1)
    end_time = datetime.datetime(2020,6,3)

    Company_tickername = "TCS"

    df = data.DataReader(name = Company_tickername, data_source = "yahoo",start = start_time, end = end_time)

    def inc_dec (c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = 'Decrease'
        else:
            value = 'Equal'
        return value
            
    df["status"] = [inc_dec (c,o) for c,o in zip(df.Close,df.Open)]
    df["Middle"] = (df.Close+df.Open)/2
    df["Height"] = abs(df.Close-df.Open)

    p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = 'scale_width')
    p.title.text = "Candlestick Chart "+"- "+(Company_tickername)
    p.title.text_font_size='20pt'
    p.title.align = 'center'
    p.grid.grid_line_alpha = 0.4

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, line_color = 'black')

    p.rect(df.index[df.status == "Increase"], df.Middle[df.status == 'Increase'], hours_12, 
        df.Height[df.status == "Increase"], fill_color = (211,211,211), line_color = 'black')

    p.rect(df.index[df.status == "Decrease"], df.Middle[df.status == 'Decrease'], hours_12, 
        df.Height[df.status == "Decrease"], fill_color = "#B22222", line_color = 'black')

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    return render_template("plot.html",script1 = script1, div1 = div1,
    cdn_js = cdn_js)   

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

