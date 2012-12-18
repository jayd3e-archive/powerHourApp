<html>
    <head>
        <title>Power Hour</title>
        <link rel="stylesheet" type="text/css" href="/style/mystyle.css"/>
    </head>
    <body>
        <div id="container">
            <div id="header"><h1>Power Hour</h1></div>

            <div id="subheader">
                <form method="post" action="/" id="search">
                    <label>Search Genre</label>
                    <input name="search" type="text" size="40" placeholder="Search..." input type="submit"/>
                </form>
                % if message:
                    <h3 style="color:red"> ${message} </h3>
                % endif
            </div>

            <div id="wrapper">
                <div id="content">
                    <div class="genres" id="left">
                        <h2> Genres </h2>
                        % for song in songs:
                            <div>
                                <form method="post" action"/">
                                <button name="button-click" class="blue-pill">
                                    ${ song.genre }
                                </button>
                                <form>
                            </div>
                        % endfor
                    </div>
                    <div id="center1"> <h2> Music Here </h2>
                        <h3> Genre Title </h3>
                        % if result:
                            <iframe src="https://embed.spotify.com/?uri=spotify:user:1245851618:playlist:${result.uri}" width="300" height="300" frameborder="0" allowtransparency="true"></iframe>
                        % else:
                            <iframe src="https://embed.spotify.com/?uri=spotify:user:1245851618:playlist:1BPrQD0h4xLZ3vHvCKlCbf&theme=white&view=coverart" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>
                        % endif
                    </div>

                    <div id="center2"> <h2> Count Down Here </h2> </div>

                    <div id="right"> <h2> Drink Counter Here </h2> </div>
                </div>
            </div>

            <div id="navigation"></div>

            <div id="extra"></div>

            <div id="footer">
                <p>Created December 2012</p>
            </div>
        </div>
    </body>
</html>

