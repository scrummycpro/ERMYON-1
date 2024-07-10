from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Response from Table ‘workout’</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5 mb-4" id="random-response-from-table-workout">Random Response from Table ‘workout’</h1>
            
            <div class="row">
                <div class="col-md-8">
                    <p class="lead">35|Title: Integrating Dips, Pull-ups, and Push-ups into a Calisthenics Regimen: A Comprehensive Approach</p>
                    <p><strong>Abstract:</strong></p>
                    <p>This paper aims to provide a comprehensive guide on integrating dips, pull-ups, and push-ups into a calisthenics regimen. The exercises are essential for building upper body strength, improving overall fitness, and enhancing muscular development. This paper will discuss the importance of these exercises, present a detailed exercise plan, examine potential supplements that may influence testosterone levels, and provide a 6-day diet and rest plan. Additionally, it will address controversies, debates, trade-offs, and side effects associated with these exercises.</p>
                    
                    <!-- More content goes here... -->
                    
                    <p><strong>References:</strong></p>
                    <ol>
                        <li>Dhurandhar, N. V., et al. “Effects of Tribulus terrestris on testosterone levels in healthy men.” Journal of Ethnopharmacology 146 (2013): 142-148.</li>
                        <li>Ferrando, A. A., et al. “D-aspartic acid supplementation increases muscle thickness during resistance training in older adults.” Journal of the International Society of Sports Nutrition 9 (2012): 42.</li>
                        <li>Schoenfeld, B. J. “Effects of ibuprofen on muscle protein synthesis after exercise.” Journal of Strength and Conditioning Research 25 (2011): 1235-1240.</li>
                    </ol>
                    
                    <p><strong>Note:</strong> This paper is intended for educational purposes only and should not be considered medical advice. Always consult with a healthcare professional before starting any new exercise or supplement regimen.</p>
                </div>
            </div>
        </div>
        
        <!-- Bootstrap JS (Optional: If you need Bootstrap JavaScript features) -->
        <!-- <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8sh+Fa3W/pXn3E3pwsj/SM7QGv3fD2hpkU8KI" crossorigin="anonymous"></script> -->
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)

