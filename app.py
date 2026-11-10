
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import webbrowser
import threading
import time
from urllib.parse import quote

# ==========================================
# ANIFLIX - YOUR ANIME AND ENTERTAINMENT HUB
# ==========================================

ANIME = """
Naruto, Naruto Shippuden, One Piece, Bleach, Dragon Ball Z,
Dragon Ball Super, Attack on Titan, Death Note, Demon Slayer,
Jujutsu Kaisen, My Hero Academia, Fullmetal Alchemist Brotherhood,
Hunter x Hunter, One Punch Man, Mob Psycho 100, Tokyo Ghoul,
Chainsaw Man, Spy x Family, Black Clover, Haikyuu, Blue Lock,
Solo Leveling, Vinland Saga, Code Geass, Steins Gate,
Your Lie in April, Violet Evergarden, Frieren Beyond Journey's End,
The Apothecary Diaries, Dr Stone, Fire Force, Fairy Tail,
Sword Art Online, Re Zero, That Time I Got Reincarnated as a Slime,
Overlord, Mushoku Tensei, Shield Hero, KonoSuba,
The Eminence in Shadow, Classroom of the Elite, Bungo Stray Dogs,
Psycho Pass, Parasyte, Erased, Monster, The Promised Neverland,
Made in Abyss, Hellsing Ultimate, Black Lagoon, Cowboy Bebop,
Samurai Champloo, Trigun, Neon Genesis Evangelion, Gurren Lagann,
JoJo's Bizarre Adventure, Yu Yu Hakusho, Inuyasha,
Rurouni Kenshin, Seven Deadly Sins, Magi, Noragami,
Blue Exorcist, Soul Eater, D Gray Man, Katekyo Hitman Reborn,
Food Wars, Kuroko's Basketball, Slam Dunk, Hajime no Ippo,
Yuri on Ice, Free!, Kaguya-sama Love Is War, Toradora,
Horimiya, Fruits Basket, Clannad, Anohana, Hyouka,
The Dangers in My Heart, Mashle, Kaiju No 8, Dandadan,
Gintama, Nichijou, Bocchi the Rock, K-On!, Sound Euphonium,
Oshi no Ko, Kakegurui, Initial D, Assassination Classroom,
Drifters, The Disastrous Life of Saiki K, Great Teacher Onizuka,
Ouran High School Host Club, Maid Sama, Komi Can't Communicate,
The Ancient Magus Bride, Ranking of Kings, Heavenly Delusion,
86 Eighty Six, Cyberpunk Edgerunners, Pluto, Zom 100,
Undead Unluck, Wind Breaker, The Elusive Samurai, Delicious in Dungeon,
Berserk, Kingdom, Baki, Kengan Ashura, Hajime no Ippo Rising
"""

MOVIES = """
The Shawshank Redemption, The Godfather, The Dark Knight,
Inception, Interstellar, The Matrix, The Fellowship of the Ring,
The Two Towers, The Return of the King, Harry Potter and the Sorcerer's Stone,
Harry Potter and the Prisoner of Azkaban, Harry Potter and the Goblet of Fire,
Harry Potter and the Deathly Hallows Part 2, Avengers Endgame,
Avengers Infinity War, Iron Man, Spider-Man No Way Home,
Spider-Man Into the Spider-Verse, Spider-Man Across the Spider-Verse,
Guardians of the Galaxy, Black Panther, Doctor Strange, Thor Ragnarok,
Captain America The Winter Soldier, Joker, The Batman, Man of Steel,
Wonder Woman, Aquaman, Dune, Dune Part Two, Oppenheimer, Barbie,
Top Gun Maverick, Mission Impossible Fallout, John Wick,
John Wick Chapter 4, Mad Max Fury Road, Gladiator, Troy, 300,
The Wolf of Wall Street, The Social Network, Whiplash, La La Land,
The Greatest Showman, Titanic, The Notebook, Pride and Prejudice,
Forrest Gump, Cast Away, The Green Mile, Saving Private Ryan,
Dunkirk, 1917, Hacksaw Ridge, The Pianist, Schindler's List,
Parasite, Train to Busan, The Conjuring, The Conjuring 2,
Insidious, Hereditary, Get Out, A Quiet Place, It, Scream,
The Shining, The Exorcist, Jurassic Park, Jurassic World,
King Kong, Godzilla Minus One, Pacific Rim, Avatar,
Avatar The Way of Water, Ready Player One, Edge of Tomorrow,
The Martian, Gravity, Arrival, Blade Runner 2049, The Prestige,
Shutter Island, Gone Girl, Knives Out, Glass Onion,
Now You See Me, The Grand Budapest Hotel, Home Alone, The Mask,
Groundhog Day, The Hangover, Superbad, 21 Jump Street,
Jumanji Welcome to the Jungle, Paddington 2, Coco, Inside Out,
Inside Out 2, Up, WALL-E, Finding Nemo, Toy Story,
The Incredibles, Ratatouille, Shrek, Puss in Boots The Last Wish,
Kung Fu Panda, How to Train Your Dragon, Frozen, Moana,
The Lion King, Despicable Me, Minions, The Super Mario Bros Movie,
The Lego Movie, The Truman Show, The Pursuit of Happyness,
Slumdog Millionaire, 3 Idiots, Dangal, RRR,
Baahubali The Beginning, Baahubali 2 The Conclusion,
KGF Chapter 1, KGF Chapter 2, Kantara, Drishyam, Drishyam 2,
Jawan, Pathaan, Chennai Express, Zindagi Na Milegi Dobara,
Taare Zameen Par, Andhadhun, 12th Fail, Interstellar,
The Equalizer, Nobody, Extraction, Extraction 2,
The Revenant, Life of Pi, The Curious Case of Benjamin Button,
The Imitation Game, Ford v Ferrari, Rush, The Bourne Identity,
The Bourne Ultimatum, Casino Royale, Skyfall, Spectre,
The Amazing Spider-Man, Spider-Man 2, Logan, Deadpool,
Deadpool 2, X-Men Days of Future Past, The Avengers,
Captain America Civil War, Ant-Man, Shang-Chi, Eternals
"""

SERIES = """
Breaking Bad, Better Call Saul, Game of Thrones, House of the Dragon,
Stranger Things, Wednesday, The Witcher, The Last of Us,
The Boys, Gen V, Reacher, Sherlock, Loki, Moon Knight,
Daredevil, The Mandalorian, Andor, The Umbrella Academy, Dark,
Money Heist, Squid Game, All of Us Are Dead, Alice in Borderland,
Kingdom, The Walking Dead, The 100, The Flash, Arrow,
Supernatural, The Originals, The Vampire Diaries, Teen Wolf,
Lucifer, The Sandman, Peaky Blinders, Narcos, The Crown,
Vikings, Vikings Valhalla, Suits, The Office, Brooklyn Nine-Nine,
Friends, How I Met Your Mother, The Big Bang Theory, Young Sheldon,
Modern Family, The Bear, The Queen's Gambit, Chernobyl,
Band of Brothers, The Pacific, Prison Break, Lost, Manifest,
The Good Doctor, House MD, Grey's Anatomy, The Rookie,
The Night Agent, Jack Ryan, The Gentlemen, Top Boy, Lupin,
The Recruit, One Piece Live Action, Avatar The Last Airbender,
Cobra Kai, The Haunting of Hill House, The Fall of the House of Usher,
From, Yellowjackets, Severance, Black Mirror, Westworld,
The Expanse, Foundation, Silo, The Peripheral, Upload,
The Good Place, Ted Lasso, Sex Education, Never Have I Ever,
Heartstopper, Bridgerton, Queen Charlotte, The Summer I Turned Pretty,
Outer Banks, The Glory, Vincenzo, Crash Landing on You,
Itaewon Class, Business Proposal, Extraordinary Attorney Woo,
The Night Manager, Sherlock Holmes, Dexter, Hannibal,
The Mentalist, Person of Interest, The Sopranos, The Wire,
House of Cards, Ozark, Fargo, True Detective, Mindhunter,
The Punisher, Jessica Jones, The Defenders, Agents of SHIELD,
Smallville, Gotham, Titans, Doom Patrol, The Flashpoint,
The Last Kingdom, Spartacus, Rome, Black Sails, The Tudors,
The Borgias, The Serpent, Bodyguard, Line of Duty,
The IT Crowd, Community, Parks and Recreation, Superstore,
Abbott Elementary, Silicon Valley, Entourage, Scrubs,
The Good Wife, Suits LA, The Lincoln Lawyer, The Diplomat,
The Recruit Season 2, Reacher Season 3, Fallout, The Penguin,
Agatha All Along, Gen V Season 2, Invincible, Arcane,
Castlevania, Blue Eye Samurai, Love Death and Robots,
The Dragon Prince, Rick and Morty, Adventure Time,
Regular Show, Gravity Falls, The Simpsons, Futurama,
South Park, Family Guy, American Dad, BoJack Horseman
"""

def get_genres(title, kind):
    # A simple genre finder. These rules keep filtering easy to understand.
    t = title.lower()

    rules = {
        "Action": ["naruto", "dragon", "bleach", "demon", "jujutsu",
                   "attack on titan", "one punch", "chainsaw", "john wick",
                   "avengers", "mission impossible", "batman", "reacher",
                   "vikings", "flash", "arrow", "deadpool"],
        "Adventure": ["one piece", "hunter", "solo leveling", "frieren",
                      "harry potter", "lord of the rings", "jumanji",
                      "jurassic", "avatar", "moana", "how to train"],
        "Romance": ["love", "your lie", "horimiya", "toradora", "notebook",
                    "titanic", "bridgerton", "heartstopper", "fruits basket"],
        "Comedy": ["konosuba", "saiki", "gintama", "nichijou", "friends",
                   "office", "brooklyn", "hangover", "superbad", "mask"],
        "Horror": ["tokyo ghoul", "parasyte", "hellsing", "conjuring",
                   "insidious", "hereditary", "scream", "shining",
                   "train to busan", "walking dead"],
        "Sci-Fi": ["steins gate", "psycho pass", "cowboy bebop", "evangelion",
                   "matrix", "interstellar", "dune", "blade runner",
                   "black mirror", "expanse", "severance"],
        "Mystery": ["death note", "monster", "erased", "hyouka", "drishyam",
                    "knives out", "shutter island", "sherlock", "dark",
                    "mindhunter"],
        "Drama": ["violet evergarden", "clannad", "anohana", "whiplash",
                  "forrest gump", "green mile", "breaking bad", "chernobyl"],
        "Fantasy": ["slime", "overlord", "mushoku", "re zero", "magi",
                    "inuyasha", "spirited", "howl", "witcher", "sandman"],
        "Sports": ["haikyuu", "blue lock", "kuroko", "slam dunk",
                   "hajime no ippo", "yuri on ice", "initial d"],
        "Animation": ["toy story", "coco", "inside out", "finding nemo",
                      "shrek", "kung fu panda", "minions", "super mario"]
    }

    found = []
    for genre, words in rules.items():
        if any(word in t for word in words):
            found.append(genre)

    if not found:
        if kind == "Anime":
            found = ["Anime", "Adventure"]
        elif kind == "Movies":
            found = ["Movies", "Drama"]
        else:
            found = ["Series", "Drama"]

    return found[:2]


def make_catalog(raw, kind):
    names = [x.strip() for x in raw.replace("\n", " ").split(",")]
    result = []
    seen = set()

    for name in names:
        if name and name.lower() not in seen:
            seen.add(name.lower())
            result.append({
                "title": name,
                "kind": kind,
                "genres": get_genres(name, kind)
            })

    return result


CATALOG = (
    make_catalog(ANIME, "Anime")
    + make_catalog(MOVIES, "Movies")
    + make_catalog(SERIES, "Series")
)

HTML = r"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ANIFLIX</title>
<style>
*{box-sizing:border-box}
body{margin:0;background:#09090e;color:white;font-family:Arial,sans-serif}
header{height:75px;background:#101016;display:flex;align-items:center;
padding:0 5%;gap:30px;position:sticky;top:0;z-index:5;
border-bottom:1px solid #292933}
.logo{font-size:30px;color:#f10d24;font-weight:900;letter-spacing:2px}
nav{display:flex;gap:20px}
button{cursor:pointer}
nav button{background:none;border:0;color:#ddd;font-size:15px}
nav button:hover{color:#f10d24}
#search{margin-left:auto;width:220px;padding:12px;border-radius:25px;
border:1px solid #444;background:#22222c;color:white}
.hero{min-height:390px;padding:65px 7%;display:flex;align-items:center;
background:linear-gradient(90deg,#09090e 5%,#09090ecc 55%,transparent),
linear-gradient(0deg,#09090e,transparent),
url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600')
center/cover}
.hero-content{max-width:620px}
.eyebrow{color:#ff4050;font-weight:bold;letter-spacing:3px}
.hero h1{font-size:55px;margin:15px 0}
.hero p{color:#ddd;line-height:1.7;font-size:17px}
.red{background:#f10d24;color:white;border:0;padding:13px 23px;
border-radius:6px;font-weight:bold}
main{padding:25px 5% 60px}
.filters{display:flex;gap:9px;flex-wrap:wrap;margin:18px 0}
.filter{background:#20202a;color:#ddd;border:1px solid #3b3b48;
padding:10px 14px;border-radius:20px}
.filter.active,.filter:hover{background:#f10d24;color:white}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:18px}
.card{background:#171720;border-radius:9px;overflow:hidden;
border:1px solid #292934;cursor:pointer;transition:.2s}
.card:hover{transform:translateY(-6px);border-color:#f10d24}
.poster{height:225px;background:linear-gradient(140deg,#301b52,#8a183d,#151522);
display:flex;align-items:center;justify-content:center;text-align:center;
padding:12px;position:relative;overflow:hidden}
.poster img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.poster strong{z-index:1;font-size:19px;text-shadow:0 2px 12px black}
.info{padding:11px}
.info h3{font-size:14px;margin:0 0 8px;white-space:nowrap;
overflow:hidden;text-overflow:ellipsis}
.info small{color:#aaa}
h2{font-size:23px}
.modal-bg{display:none;position:fixed;inset:0;background:#000c;
z-index:10;align-items:center;justify-content:center;padding:15px}
.modal{background:#1b1b25;border:1px solid #444;border-radius:14px;
width:min(430px,100%);padding:27px;text-align:center}
.modal h2{margin:14px 0}
.modal p{color:#aaa}
.modal button{width:100%;padding:14px;border:0;border-radius:6px;
font-weight:bold;margin-top:12px}
.trailer{background:#f10d24;color:white}
.site{background:#343440;color:white}
.close{background:none!important;color:#aaa;width:auto!important;
float:right;font-size:24px;padding:0!important;margin:0!important}
footer{text-align:center;color:#777;border-top:1px solid #25252d;padding:30px}
@media(max-width:650px){
header{height:auto;flex-wrap:wrap;padding:12px 4%;gap:12px}
nav{order:3;width:100%;justify-content:space-between}
#search{width:145px}
.hero h1{font-size:39px}
.hero{padding:40px 6%;min-height:330px}
.grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.poster{height:205px}
}

/* ANIFLIX - COLOURFUL POSTER DESIGN */

img {
    display: none !important;
}

.card,
.movie-card,
.anime-card,
.poster,
.poster-card,
.title-card {
    background-image: none !important;
    background: linear-gradient(135deg, #ff758c, #ff7eb3) !important;
    border: 2px solid rgba(255,255,255,0.25);
    border-radius: 18px;
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.card:nth-child(6n+1),
.movie-card:nth-child(6n+1),
.anime-card:nth-child(6n+1) {
    background: linear-gradient(135deg, #ff758c, #ff7eb3) !important;
}

.card:nth-child(6n+2),
.movie-card:nth-child(6n+2),
.anime-card:nth-child(6n+2) {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
}

.card:nth-child(6n+3),
.movie-card:nth-child(6n+3),
.anime-card:nth-child(6n+3) {
    background: linear-gradient(135deg, #43cea2, #185a9d) !important;
}

.card:nth-child(6n+4),
.movie-card:nth-child(6n+4),
.anime-card:nth-child(6n+4) {
    background: linear-gradient(135deg, #f7971e, #ffd200) !important;
}

.card:nth-child(6n+5),
.movie-card:nth-child(6n+5),
.anime-card:nth-child(6n+5) {
    background: linear-gradient(135deg, #fc466b, #3f5efb) !important;
}

.card:nth-child(6n),
.movie-card:nth-child(6n),
.anime-card:nth-child(6n) {
    background: linear-gradient(135deg, #a8ff78, #78ffd6) !important;
}

.card:hover,
.movie-card:hover,
.anime-card:hover {
    transform: translateY(-7px) scale(1.03);
    box-shadow: 0 12px 30px rgba(255,255,255,0.2);
}
</style>
</head>
<body>

<header>
<div class="logo">ANIFLIX</div>
<nav>
<button onclick="setType('All')">Home</button>
<button onclick="setType('Anime')">Anime</button>
<button onclick="setType('Movies')">Movies</button>
<button onclick="setType('Series')">Series</button>
</nav>
<input id="search" placeholder="Search titles..." oninput="render()">
</header>

<section class="hero">
<div class="hero-content">
<div class="eyebrow">WELCOME TO YOUR ENTERTAINMENT WORLD</div>
<h1>Unlimited stories.<br>One destination.</h1>
<p>Discover amazing anime, blockbuster movies and binge-worthy
series. Find your next favourite show on ANIFLIX.</p>
<button class="red" onclick="setType('All')">EXPLORE NOW</button>
</div>
</section>

<main>
<h2 id="heading">Explore everything</h2>
<div class="filters" id="types"></div>
<div class="filters" id="genres"></div>
<div class="grid" id="catalog"></div>
</main>

<footer>
ANIFLIX • Discover your next favourite story<br><br>
A fan-made entertainment discovery website. Videos are not hosted here.
</footer>

<div class="modal-bg" id="modal">
<div class="modal">
<button class="close" onclick="closeModal()">×</button>
<div class="eyebrow">ANIFLIX SELECTION</div>
<h2 id="modalTitle"></h2>
<p id="modalInfo"></p>
<button class="trailer" id="trailerButton">▶ WATCH TRAILER</button>
<button class="site" id="siteButton">↗ TAKE ME TO SITE</button>
</div>
</div>

<script>
let data=[];
let currentType="All";
let currentGenre="All";

const types=["All","Anime","Movies","Series"];
const genres=["All","Action","Adventure","Comedy","Drama","Fantasy",
"Horror","Mystery","Romance","Sci-Fi","Sports","Animation"];

function escapeHTML(text){
 return text.replace(/[&<>"']/g,c=>({
 "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"
 }[c]));
}

function setType(type){
 currentType=type;
 currentGenre="All";
 buildFilters();
 render();
 window.scrollTo({top:390,behavior:"smooth"});
}

function setGenre(genre){
 currentGenre=genre;
 buildFilters();
 render();
}

function buildFilters(){
 document.getElementById("heading").textContent=
 currentType==="All"?"Explore everything":"Explore "+currentType;

 document.getElementById("types").innerHTML=types.map(t=>
 `<button class="filter ${currentType===t?'active':''}"
 onclick="setType('${t}')">${t}</button>`).join("");

 document.getElementById("genres").innerHTML=genres.map(g=>
 `<button class="filter ${currentGenre===g?'active':''}"
 onclick="setGenre('${g}')">${g}</button>`).join("");
}

function render(){
 let query=document.getElementById("search").value.toLowerCase();

 let results=data.filter(item=>
 (currentType==="All"||item.kind===currentType)&&
 (currentGenre==="All"||item.genres.includes(currentGenre))&&
 item.title.toLowerCase().includes(query)
 );

 document.getElementById("catalog").innerHTML=results.map(item=>{
 let index=data.indexOf(item);
 return `<article class="card" onclick="openModal(${index})">
 <div class="poster" id="poster-${index}">
 <strong>${escapeHTML(item.title)}</strong>
 </div>
 <div class="info">
 <h3>${escapeHTML(item.title)}</h3>
 <small>${item.kind} • ${item.genres.join(" / ")}</small>
 </div></article>`;
 }).join("")||'<p>No titles found. Try another search or genre.</p>';

 results.forEach(item=>loadPoster(item,data.indexOf(item)));
}

let posterCache={};

async function loadPoster(item,index){
 if(posterCache[item.title]!==undefined){
  applyPoster(index,posterCache[item.title]);
  return;
 }
 try{
  let url="https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch="
  +encodeURIComponent(item.title+" film poster")
  +"&gsrlimit=1&prop=pageimages&piprop=thumbnail&pithumbsize=400&format=json&origin=*";

  let response=await fetch(url);
  let result=await response.json();
  let pages=result.query?Object.values(result.query.pages):[];
  let image=pages[0]&&pages[0].thumbnail?
  pages[0].thumbnail.source:null;

  posterCache[item.title]=image;
  applyPoster(index,image);
 }catch(error){
  posterCache[item.title]=null;
 }
}

function applyPoster(index,image){
 let box=document.getElementById("poster-"+index);
 if(!box||!image)return;
 let img=document.createElement("img");
 img.src=image;
 img.alt="";
 img.loading="lazy";
 img.onerror=()=>img.remove();
 box.prepend(img);
}

function openModal(index){
 let item=data[index];
 if(!item)return;

 document.getElementById("modalTitle").textContent=item.title;
 document.getElementById("modalInfo").textContent=
 item.kind+" • "+item.genres.join(" • ");

 document.getElementById("trailerButton").onclick=()=>{
  window.open("https://www.youtube.com/results?search_query="
  +encodeURIComponent(item.title+" official trailer"),"_blank");
 };

 document.getElementById("siteButton").onclick=()=>{
  window.open("https://www.google.com/search?q="
  +encodeURIComponent("where to watch "+item.title+" legally"),"_blank");
 };

 document.getElementById("modal").style.display="flex";
}

function closeModal(){
 document.getElementById("modal").style.display="none";
}

document.getElementById("modal").addEventListener("click",function(e){
 if(e.target===this)closeModal();
});

document.addEventListener("keydown",function(e){
 if(e.key==="Escape")closeModal();
});

async function start(){
 try{
  let response=await fetch("/catalog");
  data=await response.json();
  buildFilters();
  render();
 }catch(error){
  document.getElementById("catalog").innerHTML=
  "<p>Could not load titles. Please refresh the page.</p>";
 }
}

start();
</script>
</body>
</html>
"""


class AniflixHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/catalog":
            content = json.dumps(CATALOG).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            content = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

    def log_message(self, format, *args):
        pass


def open_website():
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    print("================================")
    print("       WELCOME TO ANIFLIX")
    print("================================")
    print("Anime:", len(make_catalog(ANIME, "Anime")))
    print("Movies:", len(make_catalog(MOVIES, "Movies")))
    print("Series:", len(make_catalog(SERIES, "Series")))
    print("Website: http://127.0.0.1:8000")
    print("Keep this window open while using ANIFLIX.")

    threading.Thread(target=open_website, daemon=True).start()

    try:
        server = HTTPServer(("127.0.0.1", 8000), AniflixHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("ANIFLIX stopped.")

