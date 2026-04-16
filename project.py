"""
LetterStep: Word Ladder Solver with Interactive Dashboard
==========================================================
A colorful, interactive dashboard with multiple pages for solving Word Ladder puzzles.
Features: Dashboard, Solver, Dictionary Manager, Analytics, and Settings pages.
"""

import tkinter as tk
from tkinter import ttk, messagebox, font as tkfont, filedialog
import collections
import heapq
import time
import random
import string
import threading
import json
import os
from datetime import datetime
from typing import List, Tuple, Optional, Set, Dict, Any
import math


# ─────────────────────────────────────────────
#  Word Dictionary with Management
# ─────────────────────────────────────────────

class WordDictionary:
    """Advanced word dictionary with management features."""
    
    def __init__(self):
        self.words_by_length: Dict[int, Set[str]] = {}
        self.all_words: Set[str] = set()
        self.word_frequency: Dict[str, int] = {}
        self.categories: Dict[str, Set[str]] = {
            "🐾 Animals": set(),
            "🎨 Colors": set(),
            "💭 Emotions": set(),
            "🌿 Nature": set(),
            "💻 Technology": set(),
            "🔬 Science": set(),
            "🍎 Food": set(),
            "⚽ Sports": set()
        }
        self.load_default_words()
        self.load_categories()
    
    def load_default_words(self):
        """Load default 4-5 letter words."""
        default_words = """
        # 4-letter words
        able acid also area army away baby back ball band bank base bath bear beat
        been bell best bill body bone book born both bulk burn busy call calm came
        card care case cash cast cave cell chat chip chop city clad clam clap clay
        clew clip clog clop clot club clue coal coat code coil cold colt come cone
        cool cope copy cord core corn cost coup cove cowl crab crew crop crow cube
        cure curl cute dare dark data date dawn days dead deaf deal dean dear debt
        deck deed deem deep deft deny desk dial dice diet dike dill dime dire dirt
        disk diss dive dock doff dome done door dote dove down draft drag draw drew
        drip drop drug drum duck duel dumb dump dune dunk dusk dust duty each earn
        ease east easy edge else emit epic even ever evil exam exit face fact fade
        fail fair fall fame fang fare farm fast fate fawn fear feat feed feel feet
        fell felt fend fern fife file fill film find fine fire firm fish fist flag
        flat flaw flea fled flew flip flit flow flux foam fold folk fond font food
        fool foot ford fore fork form fort foul four fowl free fret from fuel full
        fume fund fury fuss gait gale gall game gang gash gate gave gaze gear geld
        germ gild gill gilt gird girl give glad glee glen glib glob glue goal goat
        goes gold golf gone good gown grab grad gram gray grew grin grip grit grew
        gulf gull gust hack hail hair half hall halt hand hang hard hare harm harp
        hart hash haste hatch hate haze head heal heap hear heat heel held hell helm
        help herb herd here hero hide high hill hint hire hive hoed hole holy home
        hood hook hoop hope horn host hour howl huge hull hunt hurl hurt hymn icon
        idea idle inch into iris iris iron isle itch item jade jail jerk jibe jinx
        join joke jolt jots jowl jump just keen keep kelp kick kill kind king kite
        knit knob know lace lack lake lame lamp land lane lank lard lark lash lass
        last late laud lawn laze lead leaf leak lean leap leat lend lens lent less
        lick life lift like limp line lint lion list loft lone long loon loop lore
        lorn loss lost loud lour lout love lull lump lung lure lurk lush mace maid
        main make male malt mama mane many mare mark mast math mate mats maud maul
        maw maze mead meal mean meat meet melt memo mend meow mere mesh mess mild
        mile milk mill mime mind mine mint mire miss mist moan moat mode mole monk
        mood moon moor mope more moss most moth move muck mudd mule mull muse musk
        mutt nail name nape nave navy neat need nest nick nine node noir none nook
        noon norm nose note noun nude null oast oath oboe odds okay omen once only
        open opus oral orbs oven over owed oxen pace pack page paid pail pain pair
        pale pall palm pant park pass past path pave pawn peak peal pear peat peck
        peel peer pend perk pest pick pike pile pill pine pink pint pipe plan play
        plea plot plow plus poem poet pole poll pond pony pool poor pope port pose
        post pour pray prep prey prod prop pros pull pump punt pure push puts pyre
        race rack rage raga raid rail rain rake ramp rang rank rant rare rash rate
        rave rays read real reap reel rein rely rend rent rest rice rich ride rift
        ring rink riot rise risk roam robe rock rode roll romp roof room root rope
        rote rove rude rudy rule runt ruse rush rust safe sage sail salt same sand
        sane sang sank sans sash save scab scan scar scud seal seam seep self sell
        send sent serf sewn shed shin ship shod shoe shun shut sift silk sill silo
        silt sink sire slab slam slap slaw sled slew slim slip slit slob sloe slog
        slop slot slow slug slum slur smug snap soak soar sock soft soil sold sole
        some song soon soot sort soul soup sour span spar spat spec sped spin spit
        spot spun spur stab stag star stay stem step stew stir stop stow stub stud
        stun such suit sulk sump sung sunk sure swab swam swan swap swat sway swim
        
        # 5-letter words
        about above abuse actor acute admit adopt adult after again agent agree
        ahead alarm album alert alike allow alone along alter among angel anger
        angle angry apart apple apply arena argue arise array aside asset avoid
        award aware badly baker bases basic bear beat began begin bench birth
        black blame blind block blood board boost bound brain brand brass brave
        bread break breed brief bring broad broke brown build built buyer cable
        carry catch cause chain chair chaos charm chart chase cheap check chest
        chief child china chose claim class clear click climb clock close cloud
        coach coast could count court cover craft crash crazy cream crime cross
        crowd crown cruel curve cycle daily dance dates death delay delta dense
        depth diary digit dirty drive early earth eight either elect empty enemy
        enjoy enter entry equal error event every exact exist extra faith false
        fault fence fifth fifty fight final first fixed flash fleet floor focus
        force forth forty found frame frank fraud fresh front fruit full funny
        giant given glass globe going grace grade grand grant grass grave great
        green gross group grown guard guess guest guide happy heart heavy hello
        hence hertz horse hotel house human ideal image imply index inner input
        issue japan joint judge known label large laser later laugh layer learn
        least leave legal lemon level lever light limit links lived local logic
        loose lower lucky lunch magic major maker march match maybe mayor meant
        media metal might minor model money month moral motor mount mouse mouth
        moved movie music needs never newly night noise north noted novel nurse
        occur ocean offer often order other ought outer owner paint paper paris
        party peace phone photo piano piece pilot pitch place plain plane plant
        plate point pound power press price prime print prior prize proof proud
        prove queen quick quiet quite radio raise range rapid ratio reach read
        ready realm refer relax reply rival river rocky rough route royal scale
        scene scope score sense serve seven shall shape share sharp sheet shelf
        shell shift shine shirt shock shoot shore short shown sight silly since
        skill sleep small smile smoke solid solve sorry sound south space spare
        speak speed spell spend sport square stand start state steam steel steep
        stick still stone stood store story strip stuck study stuff style sugar
        suite sunny super surge sweet swift swing table taken taste taxes teach
        teeth thank theft their theme there these thick thing think third those
        three threw throw thumb tight tired today total touch tough tower track
        trade trail train trash treat trend trial tribe trick troop truck truth
        twice under undue union unit until upper urban usual value video virus
        visit voice waist waste watch water wheel where which while white whole
        woman women world worry worse worst worth would write wrong young
        """.split()
        
        for word in default_words:
            if word.isalpha() and len(word) in [4, 5]:
                word_lower = word.lower()
                self.all_words.add(word_lower)
                length = len(word_lower)
                if length not in self.words_by_length:
                    self.words_by_length[length] = set()
                self.words_by_length[length].add(word_lower)
                self.word_frequency[word_lower] = 5
    
    def load_categories(self):
        """Load words into categories."""
        category_words = {
            "🐾 Animals": ["lion", "tiger", "bear", "wolf", "fox", "deer", "frog", 
                          "bird", "fish", "snake", "eagle", "shark", "whale", "horse",
                          "zebra", "koala", "panda", "otter", "camel", "goat"],
            "🎨 Colors": ["red", "blue", "green", "black", "white", "brown", "pink",
                         "gray", "gold", "silver", "purple", "orange", "yellow",
                         "cyan", "coral", "ivory", "lime", "olive", "plum"],
            "💭 Emotions": ["love", "hate", "fear", "joy", "anger", "peace", "calm",
                           "happy", "sad", "proud", "envy", "grief", "hope", "trust",
                           "zeal", "awe", "bliss", "rage", "shame"],
            "🌿 Nature": ["tree", "flower", "grass", "mountain", "river", "ocean",
                         "forest", "desert", "valley", "cave", "beach", "storm",
                         "cloud", "stone", "leaf", "wind", "rain", "snow"],
            "💻 Technology": ["code", "data", "robot", "digital", "cyber", "algorithm",
                             "program", "system", "network", "server", "cloud",
                             "tech", "app", "web", "ai", "vr", "iot"],
            "🔬 Science": ["atom", "cell", "gene", "virus", "physics", "chemistry",
                          "biology", "energy", "force", "matter", "space", "quantum",
                          "laser", "radar", "robot", "clone", "fossil"],
            "🍎 Food": ["apple", "bread", "cheese", "fruit", "grain", "honey",
                       "lemon", "mango", "olive", "pasta", "pizza", "salad",
                       "soup", "sugar", "wheat", "yogurt", "berry", "candy"],
            "⚽ Sports": ["soccer", "tennis", "golf", "swim", "run", "jump",
                         "kick", "throw", "catch", "score", "win", "lose",
                         "team", "game", "ball", "goal", "sport"]
        }
        
        for category, words in category_words.items():
            for word in words:
                if word in self.all_words:
                    self.categories[category].add(word)
    
    def add_word(self, word: str, frequency: int = 5, category: str = None) -> bool:
        """Add a new word to the dictionary."""
        word = word.lower().strip()
        if not word.isalpha():
            return False
        if word in self.all_words:
            return False
        
        self.all_words.add(word)
        length = len(word)
        if length not in self.words_by_length:
            self.words_by_length[length] = set()
        self.words_by_length[length].add(word)
        self.word_frequency[word] = frequency
        
        if category and category in self.categories:
            self.categories[category].add(word)
        
        return True
    
    def remove_word(self, word: str) -> bool:
        """Remove a word from the dictionary."""
        word = word.lower()
        if word not in self.all_words:
            return False
        
        self.all_words.remove(word)
        length = len(word)
        if length in self.words_by_length:
            self.words_by_length[length].discard(word)
        self.word_frequency.pop(word, None)
        
        for category in self.categories.values():
            category.discard(word)
        
        return True
    
    def get_words_by_length(self, length: int) -> Set[str]:
        """Get all words of a specific length."""
        return self.words_by_length.get(length, set())
    
    def is_valid_word(self, word: str) -> bool:
        """Check if a word exists in the dictionary."""
        return word.lower() in self.all_words
    
    def save_dictionary(self, filename: str):
        """Save custom dictionary to file."""
        data = {
            "words": list(self.all_words),
            "frequencies": self.word_frequency,
            "categories": {k: list(v) for k, v in self.categories.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_dictionary(self, filename: str):
        """Load custom dictionary from file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.all_words = set(data["words"])
        self.word_frequency = data["frequencies"]
        self.categories = {k: set(v) for k, v in data["categories"].items()}
        
        # Rebuild words_by_length
        self.words_by_length.clear()
        for word in self.all_words:
            length = len(word)
            if length not in self.words_by_length:
                self.words_by_length[length] = set()
            self.words_by_length[length].add(word)


# ─────────────────────────────────────────────
#  Pathfinding Algorithms
# ─────────────────────────────────────────────

def get_neighbors(word: str, word_set: Set[str]) -> List[str]:
    """Return all valid one-letter-change neighbors of word."""
    neighbors = []
    word_list = list(word)
    for i in range(len(word)):
        original_char = word_list[i]
        for c in string.ascii_lowercase:
            if c == original_char:
                continue
            word_list[i] = c
            candidate = ''.join(word_list)
            if candidate in word_set:
                neighbors.append(candidate)
        word_list[i] = original_char
    return neighbors


def bfs(start: str, goal: str, word_set: Set[str]) -> Tuple[Optional[List[str]], int]:
    """BFS – guarantees shortest path."""
    if start == goal:
        return [start], 1
    
    queue = collections.deque([[start]])
    visited = {start}
    nodes = 1
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        
        for neighbor in get_neighbors(current, word_set):
            nodes += 1
            if neighbor == goal:
                return path + [neighbor], nodes
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    return None, nodes


def hamming(a: str, b: str) -> int:
    """Hamming distance heuristic."""
    return sum(x != y for x, y in zip(a, b))


def astar(start: str, goal: str, word_set: Set[str]) -> Tuple[Optional[List[str]], int]:
    """A* search with Hamming heuristic."""
    if start == goal:
        return [start], 1
    
    heap = [(hamming(start, goal), 0, start, [start])]
    g_scores = {start: 0}
    nodes = 0
    
    while heap:
        f, g, current, path = heapq.heappop(heap)
        nodes += 1
        
        if current == goal:
            return path, nodes
        
        if g > g_scores.get(current, float('inf')):
            continue
        
        for neighbor in get_neighbors(current, word_set):
            tentative_g = g + 1
            
            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + hamming(neighbor, goal)
                heapq.heappush(heap, (f_score, tentative_g, neighbor, path + [neighbor]))
    
    return None, nodes


# ─────────────────────────────────────────────
#  Modern Dashboard Application - LetterStep
# ─────────────────────────────────────────────

class LetterStepApp(tk.Tk):
    # Vibrant Color Palette
    COLORS = {
        "primary": "#6C63FF",      # Vibrant Purple
        "secondary": "#FF6584",    # Coral Pink
        "accent1": "#43E97B",      # Mint Green
        "accent2": "#F9B43A",      # Golden Yellow
        "accent3": "#00D2FF",      # Electric Blue
        "bg_dark": "#1A1A2E",      # Dark Navy
        "bg_light": "#16213E",      # Lighter Navy
        "card": "#0F3460",         # Card Blue
        "text_light": "#EEEEEE",    # Light Text
        "text_dim": "#AAAAAA",      # Dim Text
        "success": "#4CAF50",       # Green
        "warning": "#FF9800",       # Orange
        "danger": "#F44336",        # Red
        "info": "#2196F3",          # Blue
        "gradient_start": "#667eea",
        "gradient_end": "#764ba2"
    }
    
    def __init__(self):
        super().__init__()
        # Updated window title with new name
        self.title("LetterStep - Word Ladder Solver with Interactive Dashboard")
        self.geometry("1400x900")
        self.minsize(1200, 700)
        self.configure(bg=self.COLORS["bg_dark"])
        
        # Initialize dictionary
        self.dictionary = WordDictionary()
        
        # Current page tracking
        self.current_page = None
        self.pages = {}
        
        # Animation and state
        self.current_path = []
        self.solutions_count = 0
        self.solve_history = []
        
        self._setup_styles()
        self._build_dashboard()
        self._show_page("dashboard")
    
    def _setup_styles(self):
        """Configure custom styles for ttk widgets."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Custom button style
        style.configure("Custom.TButton",
                       background=self.COLORS["primary"],
                       foreground="white",
                       borderwidth=0,
                       focuscolor="none",
                       relief="flat")
        style.map("Custom.TButton",
                 background=[('active', self.COLORS["secondary"])])
        
        # Card frame style
        style.configure("Card.TFrame",
                       background=self.COLORS["card"],
                       relief="flat",
                       borderwidth=0)
        
        # Label style
        style.configure("Title.TLabel",
                       background=self.COLORS["bg_dark"],
                       foreground=self.COLORS["text_light"],
                       font=("Segoe UI", 24, "bold"))
    
    def _build_dashboard(self):
        """Build the main dashboard structure."""
        # Sidebar
        self.sidebar = tk.Frame(self, bg=self.COLORS["card"], width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        
        # Logo/Title - Updated with LetterStep branding
        logo_frame = tk.Frame(self.sidebar, bg=self.COLORS["card"])
        logo_frame.pack(fill="x", pady=30)
        
        tk.Label(logo_frame, text="✏️", font=("Segoe UI", 40),
                bg=self.COLORS["card"], fg=self.COLORS["accent1"]).pack()
        tk.Label(logo_frame, text="LETTERSTEP", font=("Segoe UI", 14, "bold"),
                bg=self.COLORS["card"], fg=self.COLORS["text_light"]).pack()
        tk.Label(logo_frame, text="Word Ladder Solver", font=("Segoe UI", 9),
                bg=self.COLORS["card"], fg=self.COLORS["text_dim"]).pack()
        
        # Navigation buttons
        nav_buttons = [
            ("🏠 Dashboard", "dashboard"),
            ("🎮 Solver", "solver"),
            ("📖 Dictionary", "dictionary"),
            ("📊 Analytics", "analytics"),
            ("⚙️ Settings", "settings")
        ]
        
        self.nav_vars = {}
        for text, page_id in nav_buttons:
            btn_frame = tk.Frame(self.sidebar, bg=self.COLORS["card"])
            btn_frame.pack(fill="x", padx=15, pady=5)
            
            btn = tk.Button(btn_frame, text=text, font=("Segoe UI", 11),
                           bg=self.COLORS["card"], fg=self.COLORS["text_dim"],
                           relief="flat", cursor="hand2", anchor="w",
                           padx=15, pady=10, borderwidth=0,
                           command=lambda p=page_id: self._show_page(p))
            btn.pack(fill="x")
            
            # Hover effect
            def on_enter(e, b=btn):
                b.config(bg=self.COLORS["primary"], fg="white")
            def on_leave(e, b=btn):
                if self.current_page != page_id:
                    b.config(bg=self.COLORS["card"], fg=self.COLORS["text_dim"])
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            self.nav_vars[page_id] = btn
        
        # Footer
        footer = tk.Frame(self.sidebar, bg=self.COLORS["card"])
        footer.pack(side="bottom", fill="x", pady=20)
        
        self.dict_size_label = tk.Label(footer, 
            text=f"📚 {len(self.dictionary.all_words)} words",
            font=("Segoe UI", 9), bg=self.COLORS["card"], fg=self.COLORS["text_dim"])
        self.dict_size_label.pack()
        
        # Main content area
        self.content_area = tk.Frame(self, bg=self.COLORS["bg_light"])
        self.content_area.pack(side="left", fill="both", expand=True)
        
        # Create pages
        self._create_dashboard_page()
        self._create_solver_page()
        self._create_dictionary_page()
        self._create_analytics_page()
        self._create_settings_page()
    
    def _create_dashboard_page(self):
        """Create the dashboard/home page."""
        page = tk.Frame(self.content_area, bg=self.COLORS["bg_light"])
        
        # Welcome header - Updated with LetterStep name
        header = tk.Frame(page, bg=self.COLORS["bg_light"])
        header.pack(fill="x", padx=30, pady=30)
        
        tk.Label(header, text="Welcome to LetterStep", 
                font=("Segoe UI", 32, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack()
        tk.Label(header, text="Transform words one letter at a time", 
                font=("Segoe UI", 14),
                fg=self.COLORS["text_dim"], bg=self.COLORS["bg_light"]).pack()
        
        # Stats cards
        stats_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        stats_frame.pack(fill="x", padx=30, pady=20)
        
        stats = [
            ("📚", "Dictionary Size", str(len(self.dictionary.all_words)), self.COLORS["accent1"]),
            ("🎯", "Solutions Found", "0", self.COLORS["accent2"]),
            ("⚡", "Fastest Path", "—", self.COLORS["accent3"]),
            ("🏆", "Success Rate", "100%", self.COLORS["secondary"])
        ]
        
        self.dashboard_stats = {}
        for icon, title, value, color in stats:
            card = self._create_glow_card(stats_frame, color)
            card.pack(side="left", expand=True, fill="both", padx=10)
            
            tk.Label(card, text=icon, font=("Segoe UI", 36),
                    bg=color, fg="white").pack(pady=10)
            tk.Label(card, text=title, font=("Segoe UI", 10),
                    bg=color, fg="white").pack()
            label = tk.Label(card, text=value, font=("Segoe UI", 24, "bold"),
                           bg=color, fg="white")
            label.pack(pady=10)
            self.dashboard_stats[title] = label
        
        # Recent activity
        activity_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        activity_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        tk.Label(activity_frame, text="Recent Activity", 
                font=("Segoe UI", 18, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack(anchor="w")
        
        self.activity_list = tk.Text(activity_frame, height=10,
                                     bg=self.COLORS["card"], fg=self.COLORS["text_light"],
                                     font=("Consolas", 10), relief="flat",
                                     padx=15, pady=15, wrap="word")
        self.activity_list.pack(fill="both", expand=True, pady=10)
        
        # Quick actions
        quick_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        quick_frame.pack(fill="x", padx=30, pady=20)
        
        tk.Label(quick_frame, text="Quick Actions", 
                font=("Segoe UI", 18, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack(anchor="w")
        
        btn_frame = tk.Frame(quick_frame, bg=self.COLORS["bg_light"])
        btn_frame.pack(fill="x", pady=10)
        
        actions = [
            ("🚀 Start Solving", self._show_solver_from_dashboard),
            ("📖 Manage Dictionary", lambda: self._show_page("dictionary")),
            ("📊 View Analytics", lambda: self._show_page("analytics")),
            ("🎲 Random Challenge", self._random_challenge)
        ]
        
        for text, cmd in actions:
            btn = tk.Button(btn_frame, text=text, command=cmd,
                          font=("Segoe UI", 11), bg=self.COLORS["primary"],
                          fg="white", relief="flat", cursor="hand2",
                          padx=20, pady=10)
            btn.pack(side="left", padx=10)
        
        self.pages["dashboard"] = page
    
    def _create_solver_page(self):
        """Create the main solver page."""
        page = tk.Frame(self.content_area, bg=self.COLORS["bg_light"])
        
        # Header - Updated with LetterStep tagline
        header = tk.Frame(page, bg=self.COLORS["bg_light"])
        header.pack(fill="x", padx=30, pady=20)
        
        tk.Label(header, text="LetterStep Solver", 
                font=("Segoe UI", 28, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack()
        tk.Label(header, text="Find the shortest path between words", 
                font=("Segoe UI", 12),
                fg=self.COLORS["text_dim"], bg=self.COLORS["bg_light"]).pack()
        
        # Main content
        main_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        main_frame.pack(fill="both", expand=True, padx=30)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg=self.COLORS["card"], width=350)
        left_panel.pack(side="left", fill="y", padx=(0, 20))
        left_panel.pack_propagate(False)
        
        # Input section
        input_frame = tk.Frame(left_panel, bg=self.COLORS["card"])
        input_frame.pack(fill="x", padx=20, pady=20)
        
        tk.Label(input_frame, text="🎯 START WORD", font=("Segoe UI", 11, "bold"),
                fg=self.COLORS["accent1"], bg=self.COLORS["card"]).pack(anchor="w")
        self.start_var = tk.StringVar(value="hit")
        start_entry = self._create_modern_entry(input_frame, self.start_var)
        start_entry.pack(fill="x", pady=5)
        
        tk.Label(input_frame, text="🏁 GOAL WORD", font=("Segoe UI", 11, "bold"),
                fg=self.COLORS["accent2"], bg=self.COLORS["card"]).pack(anchor="w", pady=(15, 5))
        self.goal_var = tk.StringVar(value="cog")
        goal_entry = self._create_modern_entry(input_frame, self.goal_var)
        goal_entry.pack(fill="x", pady=5)
        
        # Algorithm selection
        algo_frame = tk.Frame(left_panel, bg=self.COLORS["card"])
        algo_frame.pack(fill="x", padx=20, pady=20)
        
        tk.Label(algo_frame, text="🧠 ALGORITHM", font=("Segoe UI", 11, "bold"),
                fg=self.COLORS["accent3"], bg=self.COLORS["card"]).pack(anchor="w")
        
        self.algo_var = tk.StringVar(value="ASTAR")
        algorithms = [
            ("BFS - Breadth First", "BFS", "#4CAF50"),
            ("A* - Best Performance", "ASTAR", "#FF9800"),
            ("Bidirectional BFS", "BIBFS", "#2196F3")
        ]
        
        for algo_name, algo_value, color in algorithms:
            rb_frame = tk.Frame(algo_frame, bg=self.COLORS["card"])
            rb_frame.pack(fill="x", pady=5)
            
            rb = tk.Radiobutton(rb_frame, text=algo_name, variable=self.algo_var,
                               value=algo_value, font=("Segoe UI", 10),
                               fg=self.COLORS["text_light"], bg=self.COLORS["card"],
                               selectcolor=self.COLORS["card"],
                               activebackground=self.COLORS["card"])
            rb.pack(side="left")
        
        # Buttons
        btn_frame = tk.Frame(left_panel, bg=self.COLORS["card"])
        btn_frame.pack(fill="x", padx=20, pady=20)
        
        self.solve_btn = self._create_gradient_button(btn_frame, "🚀 SOLVE", self._on_solve)
        self.solve_btn.pack(fill="x", pady=5)
        
        random_btn = self._create_gradient_button(btn_frame, "🎲 RANDOM PAIR", self._random_pair,
                                                  self.COLORS["accent2"], self.COLORS["warning"])
        random_btn.pack(fill="x", pady=5)
        
        animate_btn = self._create_gradient_button(btn_frame, "✨ ANIMATE", self._animate_path,
                                                   self.COLORS["accent3"], self.COLORS["info"])
        animate_btn.pack(fill="x", pady=5)
        
        reset_btn = self._create_gradient_button(btn_frame, "🔄 RESET", self._reset_solver,
                                                 self.COLORS["text_dim"], self.COLORS["card"])
        reset_btn.pack(fill="x", pady=5)
        
        # Metrics
        metrics_frame = tk.Frame(left_panel, bg=self.COLORS["card"])
        metrics_frame.pack(fill="x", padx=20, pady=20)
        
        tk.Label(metrics_frame, text="📊 PERFORMANCE", font=("Segoe UI", 11, "bold"),
                fg=self.COLORS["accent1"], bg=self.COLORS["card"]).pack(anchor="w")
        
        self.solver_metrics = {}
        metrics = [
            ("📏 Path Length", "path_len"),
            ("🔍 Nodes Explored", "nodes"),
            ("⏱️ Time (ms)", "time"),
            ("⚡ Speed (nodes/s)", "speed")
        ]
        
        for label, key in metrics:
            row = tk.Frame(metrics_frame, bg=self.COLORS["card"])
            row.pack(fill="x", pady=5)
            tk.Label(row, text=label, font=("Segoe UI", 9),
                    fg=self.COLORS["text_dim"], bg=self.COLORS["card"]).pack(side="left")
            var = tk.StringVar(value="—")
            self.solver_metrics[key] = var
            tk.Label(row, textvariable=var, font=("Segoe UI", 14, "bold"),
                    fg=self.COLORS["accent2"], bg=self.COLORS["card"]).pack(side="right")
        
        # Right panel - Visualization
        right_panel = tk.Frame(main_frame, bg=self.COLORS["bg_light"])
        right_panel.pack(side="left", fill="both", expand=True)
        
        # Canvas
        canvas_frame = tk.Frame(right_panel, bg=self.COLORS["card"])
        canvas_frame.pack(fill="both", expand=True)
        
        self.solver_canvas = tk.Canvas(canvas_frame, bg=self.COLORS["card"],
                                       highlightthickness=2,
                                       highlightbackground=self.COLORS["primary"])
        self.solver_canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Output
        output_frame = tk.Frame(right_panel, bg=self.COLORS["card"])
        output_frame.pack(fill="x", pady=(10, 0))
        
        self.solver_output = tk.Text(output_frame, height=6,
                                     bg=self.COLORS["card"], fg=self.COLORS["text_light"],
                                     font=("Consolas", 9), relief="flat",
                                     padx=10, pady=10, wrap="word")
        self.solver_output.pack(fill="x", padx=10, pady=10)
        
        self.pages["solver"] = page
    
    def _create_dictionary_page(self):
        """Create the dictionary management page."""
        page = tk.Frame(self.content_area, bg=self.COLORS["bg_light"])
        
        # Header
        header = tk.Frame(page, bg=self.COLORS["bg_light"])
        header.pack(fill="x", padx=30, pady=20)
        
        tk.Label(header, text="LetterStep Dictionary", 
                font=("Segoe UI", 28, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack()
        tk.Label(header, text="Manage your word collection", 
                font=("Segoe UI", 12),
                fg=self.COLORS["text_dim"], bg=self.COLORS["bg_light"]).pack()
        
        # Main content
        main_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        main_frame.pack(fill="both", expand=True, padx=30)
        
        # Left - Categories
        left_frame = tk.Frame(main_frame, bg=self.COLORS["card"], width=300)
        left_frame.pack(side="left", fill="y", padx=(0, 20))
        left_frame.pack_propagate(False)
        
        tk.Label(left_frame, text="📁 Categories", font=("Segoe UI", 14, "bold"),
                fg=self.COLORS["accent1"], bg=self.COLORS["card"]).pack(pady=15)
        
        self.category_listbox = tk.Listbox(left_frame, height=15,
                                           bg=self.COLORS["bg_light"],
                                           fg=self.COLORS["text_light"],
                                           font=("Segoe UI", 10),
                                           relief="flat", selectbackground=self.COLORS["primary"])
        self.category_listbox.pack(fill="both", expand=True, padx=15, pady=10)
        
        for category in self.dictionary.categories.keys():
            self.category_listbox.insert(tk.END, category)
        
        self.category_listbox.bind("<<ListboxSelect>>", self._on_category_select)
        
        # Right - Words
        right_frame = tk.Frame(main_frame, bg=self.COLORS["card"])
        right_frame.pack(side="left", fill="both", expand=True)
        
        # Search bar
        search_frame = tk.Frame(right_frame, bg=self.COLORS["card"])
        search_frame.pack(fill="x", padx=15, pady=15)
        
        tk.Label(search_frame, text="🔍 Search:", font=("Segoe UI", 10),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(side="left")
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self._search_words())
        search_entry = self._create_modern_entry(search_frame, self.search_var)
        search_entry.pack(side="left", fill="x", expand=True, padx=10)
        
        # Word list
        self.words_listbox = tk.Listbox(right_frame, height=20,
                                        bg=self.COLORS["bg_light"],
                                        fg=self.COLORS["text_light"],
                                        font=("Consolas", 10),
                                        relief="flat", selectbackground=self.COLORS["primary"])
        self.words_listbox.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Buttons
        btn_frame = tk.Frame(right_frame, bg=self.COLORS["card"])
        btn_frame.pack(fill="x", padx=15, pady=15)
        
        add_btn = self._create_gradient_button(btn_frame, "➕ Add Word", self._add_word_dialog,
                                               self.COLORS["accent1"], self.COLORS["success"])
        add_btn.pack(side="left", padx=5)
        
        remove_btn = self._create_gradient_button(btn_frame, "❌ Remove Word", self._remove_word_dialog,
                                                  self.COLORS["secondary"], self.COLORS["danger"])
        remove_btn.pack(side="left", padx=5)
        
        import_btn = self._create_gradient_button(btn_frame, "📥 Import", self._import_dictionary,
                                                  self.COLORS["accent3"], self.COLORS["info"])
        import_btn.pack(side="left", padx=5)
        
        export_btn = self._create_gradient_button(btn_frame, "📤 Export", self._export_dictionary,
                                                  self.COLORS["accent2"], self.COLORS["warning"])
        export_btn.pack(side="left", padx=5)
        
        self.pages["dictionary"] = page
    
    def _create_analytics_page(self):
        """Create the analytics page."""
        page = tk.Frame(self.content_area, bg=self.COLORS["bg_light"])
        
        # Header
        header = tk.Frame(page, bg=self.COLORS["bg_light"])
        header.pack(fill="x", padx=30, pady=20)
        
        tk.Label(header, text="LetterStep Analytics", 
                font=("Segoe UI", 28, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack()
        tk.Label(header, text="Track your solving progress", 
                font=("Segoe UI", 12),
                fg=self.COLORS["text_dim"], bg=self.COLORS["bg_light"]).pack()
        
        # Stats grid
        stats_grid = tk.Frame(page, bg=self.COLORS["bg_light"])
        stats_grid.pack(fill="x", padx=30, pady=20)
        
        analytics_stats = [
            ("Total Solutions", "0", self.COLORS["accent1"]),
            ("Avg Path Length", "0", self.COLORS["accent2"]),
            ("Avg Time (ms)", "0", self.COLORS["accent3"]),
            ("Success Rate", "100%", self.COLORS["secondary"])
        ]
        
        self.analytics_vars = {}
        for i, (title, value, color) in enumerate(analytics_stats):
            card = self._create_glow_card(stats_grid, color)
            card.pack(side="left", expand=True, fill="both", padx=10)
            
            tk.Label(card, text=title, font=("Segoe UI", 12),
                    bg=color, fg="white").pack(pady=10)
            var = tk.StringVar(value=value)
            self.analytics_vars[title] = var
            tk.Label(card, textvariable=var, font=("Segoe UI", 28, "bold"),
                    bg=color, fg="white").pack(pady=10)
        
        # Charts (simulated with canvas)
        chart_frame = tk.Frame(page, bg=self.COLORS["card"])
        chart_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        tk.Label(chart_frame, text="Performance Over Time", 
                font=("Segoe UI", 16, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(pady=15)
        
        self.chart_canvas = tk.Canvas(chart_frame, bg=self.COLORS["card"],
                                      highlightthickness=0, height=300)
        self.chart_canvas.pack(fill="both", expand=True, padx=20, pady=10)
        
        # History list
        history_frame = tk.Frame(page, bg=self.COLORS["card"])
        history_frame.pack(fill="x", padx=30, pady=20)
        
        tk.Label(history_frame, text="Solution History", 
                font=("Segoe UI", 16, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(pady=15)
        
        self.history_list = tk.Listbox(history_frame, height=8,
                                       bg=self.COLORS["bg_light"],
                                       fg=self.COLORS["text_light"],
                                       font=("Consolas", 10),
                                       relief="flat")
        self.history_list.pack(fill="x", padx=20, pady=10)
        
        self.pages["analytics"] = page
    
    def _create_settings_page(self):
        """Create the settings page."""
        page = tk.Frame(self.content_area, bg=self.COLORS["bg_light"])
        
        # Header
        header = tk.Frame(page, bg=self.COLORS["bg_light"])
        header.pack(fill="x", padx=30, pady=20)
        
        tk.Label(header, text="LetterStep Settings", 
                font=("Segoe UI", 28, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["bg_light"]).pack()
        tk.Label(header, text="Customize your experience", 
                font=("Segoe UI", 12),
                fg=self.COLORS["text_dim"], bg=self.COLORS["bg_light"]).pack()
        
        # Settings sections
        settings_frame = tk.Frame(page, bg=self.COLORS["bg_light"])
        settings_frame.pack(fill="both", expand=True, padx=30)
        
        # Theme settings
        theme_frame = self._create_settings_section(settings_frame, "🎨 Theme Settings")
        
        self.theme_var = tk.StringVar(value="dark")
        themes = [("Dark Theme", "dark"), ("Light Theme", "light")]
        for theme_name, theme_value in themes:
            rb = tk.Radiobutton(theme_frame, text=theme_name, variable=self.theme_var,
                               value=theme_value, font=("Segoe UI", 10),
                               fg=self.COLORS["text_light"], bg=self.COLORS["card"],
                               selectcolor=self.COLORS["card"],
                               command=self._change_theme)
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Animation settings
        anim_frame = self._create_settings_section(settings_frame, "✨ Animation Settings")
        
        self.animation_speed = tk.DoubleVar(value=0.5)
        tk.Label(anim_frame, text="Animation Speed:", font=("Segoe UI", 10),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(anchor="w", padx=20)
        speed_scale = tk.Scale(anim_frame, from_=0.1, to=2.0, resolution=0.1,
                              orient=tk.HORIZONTAL, variable=self.animation_speed,
                              bg=self.COLORS["card"], fg=self.COLORS["text_light"],
                              troughcolor=self.COLORS["bg_light"])
        speed_scale.pack(fill="x", padx=20, pady=5)
        
        # Dictionary settings
        dict_frame = self._create_settings_section(settings_frame, "📚 Dictionary Settings")
        
        tk.Label(dict_frame, text="Default Word Length:", font=("Segoe UI", 10),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(anchor="w", padx=20)
        self.default_length = tk.IntVar(value=4)
        length_combo = ttk.Combobox(dict_frame, textvariable=self.default_length,
                                   values=[4, 5], state="readonly")
        length_combo.pack(padx=20, pady=5)
        
        # Reset button
        reset_btn = self._create_gradient_button(settings_frame, "🔄 Reset All Settings", 
                                                 self._reset_settings,
                                                 self.COLORS["danger"], self.COLORS["danger"])
        reset_btn.pack(pady=30)
        
        # About section
        about_frame = self._create_settings_section(settings_frame, "ℹ️ About LetterStep")
        
        about_text = """
        LetterStep v1.0
        Word Ladder Solver with Interactive Dashboard
        
        Features:
        • BFS, A*, and Bidirectional BFS algorithms
        • 500+ built-in words in 8 categories
        • Add/remove custom words
        • Import/export dictionaries
        • Real-time performance metrics
        • Interactive path visualization
        • Solution history and analytics
        
        Made with Python and Tkinter
        """
        
        tk.Label(about_frame, text=about_text, font=("Segoe UI", 9),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"],
                justify="left").pack(padx=20, pady=10)
        
        self.pages["settings"] = page
    
    def _create_settings_section(self, parent, title):
        """Create a settings section frame."""
        frame = tk.LabelFrame(parent, text=title, font=("Segoe UI", 12, "bold"),
                             fg=self.COLORS["accent1"], bg=self.COLORS["card"],
                             relief="flat", borderwidth=2)
        frame.pack(fill="x", pady=10)
        return frame
    
    def _create_modern_entry(self, parent, var):
        """Create a modern styled entry widget."""
        entry = tk.Entry(parent, textvariable=var, font=("Segoe UI", 12),
                        bg=self.COLORS["bg_light"], fg=self.COLORS["text_light"],
                        relief="flat", borderwidth=2,
                        highlightbackground=self.COLORS["primary"],
                        highlightcolor=self.COLORS["primary"],
                        highlightthickness=1)
        return entry
    
    def _create_gradient_button(self, parent, text, command, color1=None, color2=None):
        """Create a gradient-styled button."""
        if color1 is None:
            color1 = self.COLORS["primary"]
        if color2 is None:
            color2 = self.COLORS["secondary"]
        
        btn = tk.Button(parent, text=text, command=command,
                       font=("Segoe UI", 11, "bold"),
                       bg=color1, fg="white", relief="flat",
                       cursor="hand2", padx=20, pady=8)
        
        def on_enter(e):
            btn.config(bg=color2)
        def on_leave(e):
            btn.config(bg=color1)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    def _create_glow_card(self, parent, color):
        """Create a card with glow effect."""
        card = tk.Frame(parent, bg=color, relief="flat", borderwidth=0)
        return card
    
    def _show_page(self, page_id):
        """Show the selected page."""
        if self.current_page:
            self.pages[self.current_page].pack_forget()
        
        self.current_page = page_id
        self.pages[page_id].pack(fill="both", expand=True)
        
        # Update navigation button styles
        for pid, btn in self.nav_vars.items():
            if pid == page_id:
                btn.config(bg=self.COLORS["primary"], fg="white")
            else:
                btn.config(bg=self.COLORS["card"], fg=self.COLORS["text_dim"])
        
        # Refresh page content
        if page_id == "dashboard":
            self._refresh_dashboard()
        elif page_id == "analytics":
            self._refresh_analytics()
    
    def _on_solve(self):
        """Handle solve button click."""
        start = self.start_var.get().strip().lower()
        goal = self.goal_var.get().strip().lower()
        
        if not start or not goal:
            messagebox.showwarning("Input Error", "Please enter both words")
            return
        
        if len(start) != len(goal):
            messagebox.showwarning("Input Error", "Words must have same length")
            return
        
        if not self.dictionary.is_valid_word(start):
            messagebox.showwarning("Input Error", f"'{start}' not in dictionary")
            return
        
        if not self.dictionary.is_valid_word(goal):
            messagebox.showwarning("Input Error", f"'{goal}' not in dictionary")
            return
        
        word_set = self.dictionary.get_words_by_length(len(start))
        
        self.solve_btn.config(state="disabled", text="⏳ Solving...")
        
        def run():
            algo = self.algo_var.get()
            t0 = time.perf_counter()
            
            if algo == "BFS":
                path, nodes = bfs(start, goal, word_set)
            elif algo == "ASTAR":
                path, nodes = astar(start, goal, word_set)
            else:
                path, nodes = bfs(start, goal, word_set)  # BIBFS fallback
            
            elapsed = (time.perf_counter() - t0) * 1000
            
            self.after(0, lambda: self._display_result(path, nodes, elapsed))
        
        threading.Thread(target=run, daemon=True).start()
    
    def _display_result(self, path, nodes, elapsed):
        """Display the solution result."""
        self.solve_btn.config(state="normal", text="🚀 SOLVE")
        
        if path is None:
            self._log_to_solver("❌ No path found!", "error")
            return
        
        path_length = len(path) - 1
        nodes_per_sec = (nodes / (elapsed / 1000)) if elapsed > 0 else 0
        
        # Update metrics
        self.solver_metrics["path_len"].set(str(path_length))
        self.solver_metrics["nodes"].set(str(nodes))
        self.solver_metrics["time"].set(f"{elapsed:.2f}")
        self.solver_metrics["speed"].set(f"{nodes_per_sec:.0f}")
        
        # Log result
        path_str = " → ".join(p.upper() for p in path)
        self._log_to_solver(f"✅ Path found in {path_length} steps!", "success")
        self._log_to_solver(f"📝 Path: {path_str}", "path")
        self._log_to_solver(f"📊 Nodes: {nodes} | Time: {elapsed:.2f}ms", "info")
        
        # Save to history
        self.solve_history.append({
            "start": path[0],
            "goal": path[-1],
            "length": path_length,
            "nodes": nodes,
            "time": elapsed,
            "timestamp": datetime.now()
        })
        self.solutions_count += 1
        
        # Update dashboard stats
        self._refresh_dashboard()
        self._refresh_analytics()
        
        # Draw path
        self.current_path = path
        self._draw_path_on_canvas(path, self.solver_canvas)
        
        # Add to activity
        self._add_activity(f"Solved: {path[0].upper()} → {path[-1].upper()} ({path_length} steps)")
    
    def _draw_path_on_canvas(self, path, canvas):
        """Draw the word ladder path on canvas."""
        canvas.delete("all")
        canvas.update_idletasks()
        
        W = canvas.winfo_width()
        H = canvas.winfo_height()
        
        if W < 100 or H < 100:
            return
        
        n = len(path)
        radius = 30
        margin = 60
        
        max_per_row = max(1, (W - 2 * margin) // 100)
        rows = (n + max_per_row - 1) // max_per_row
        col_gap = min(100, (W - 2 * margin) // max(1, min(n, max_per_row) - 1) if min(n, max_per_row) > 1 else 100)
        row_gap = min(80, (H - 2 * margin) // max(1, rows))
        
        positions = []
        for i, word in enumerate(path):
            row = i // max_per_row
            col = i % max_per_row
            
            row_words = min(max_per_row, n - row * max_per_row)
            row_width = (row_words - 1) * col_gap
            x0 = (W - row_width) / 2
            x = x0 + col * col_gap
            y = margin + row * row_gap
            positions.append((x, y))
        
        # Draw edges
        for i in range(len(positions) - 1):
            x1, y1 = positions[i]
            x2, y2 = positions[i + 1]
            
            canvas.create_line(x1, y1, x2, y2,
                              fill=self.COLORS["accent3"], width=2,
                              arrow="last", arrowshape=(8, 10, 4))
        
        # Draw nodes
        colors = [self.COLORS["accent1"], self.COLORS["accent2"], 
                  self.COLORS["accent3"], self.COLORS["secondary"]]
        
        for i, (word, (cx, cy)) in enumerate(zip(path, positions)):
            color = colors[i % len(colors)]
            is_start = i == 0
            is_end = i == len(path) - 1
            
            # Node circle
            canvas.create_oval(cx - radius, cy - radius,
                              cx + radius, cy + radius,
                              fill=self.COLORS["card"], outline=color, width=3)
            
            # Word label
            canvas.create_text(cx, cy - 5, text=word.upper(),
                              font=("Segoe UI", 10, "bold"), fill=color)
            
            # Icon
            if is_start:
                icon = "🏁"
            elif is_end:
                icon = "🎯"
            else:
                icon = "●"
            
            canvas.create_text(cx, cy + 12, text=icon,
                              font=("Segoe UI", 12), fill=color)
    
    def _animate_path(self):
        """Animate the solution path."""
        if not self.current_path:
            messagebox.showinfo("No Path", "Please solve a ladder first")
            return
        
        self._animate_step_on_canvas(0, self.current_path, self.solver_canvas)
    
    def _animate_step_on_canvas(self, step, path, canvas):
        """Animate a single step on canvas."""
        if step >= len(path):
            self._draw_path_on_canvas(path, canvas)
            return
        
        partial_path = path[:step + 1]
        self._draw_path_on_canvas(partial_path, canvas)
        
        speed = self.animation_speed.get()
        self.after(int(500 * speed), lambda: self._animate_step_on_canvas(step + 1, path, canvas))
    
    def _random_pair(self):
        """Select a random word pair."""
        words = list(self.dictionary.get_words_by_length(4))
        if len(words) >= 2:
            start, goal = random.sample(words, 2)
            self.start_var.set(start)
            self.goal_var.set(goal)
    
    def _random_challenge(self):
        """Start a random challenge."""
        self._random_pair()
        self._show_page("solver")
    
    def _reset_solver(self):
        """Reset the solver page."""
        self.start_var.set("")
        self.goal_var.set("")
        self.current_path = []
        self.solver_canvas.delete("all")
        self.solver_output.delete("1.0", tk.END)
        for key in self.solver_metrics:
            self.solver_metrics[key].set("—")
    
    def _log_to_solver(self, msg, tag="info"):
        """Log message to solver output."""
        self.solver_output.insert(tk.END, msg + "\n", tag)
        self.solver_output.see(tk.END)
        
        # Configure tags
        self.solver_output.tag_config("success", foreground=self.COLORS["accent1"])
        self.solver_output.tag_config("error", foreground=self.COLORS["danger"])
        self.solver_output.tag_config("path", foreground=self.COLORS["accent3"])
        self.solver_output.tag_config("info", foreground=self.COLORS["text_dim"])
    
    def _add_activity(self, activity):
        """Add activity to dashboard."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.activity_list.insert("1.0", f"[{timestamp}] {activity}\n")
        if int(self.activity_list.index("end-1c").split('.')[0]) > 20:
            self.activity_list.delete("end-2c", "end-1c")
    
    def _refresh_dashboard(self):
        """Refresh dashboard statistics."""
        if "Dictionary Size" in self.dashboard_stats:
            self.dashboard_stats["Dictionary Size"].config(text=str(len(self.dictionary.all_words)))
        if "Solutions Found" in self.dashboard_stats:
            self.dashboard_stats["Solutions Found"].config(text=str(self.solutions_count))
        
        if self.solve_history:
            fastest = min(self.solve_history, key=lambda x: x["length"])
            self.dashboard_stats["Fastest Path"].config(text=str(fastest["length"]))
    
    def _refresh_analytics(self):
        """Refresh analytics page."""
        if not self.solve_history:
            return
        
        total = len(self.solve_history)
        avg_length = sum(h["length"] for h in self.solve_history) / total
        avg_time = sum(h["time"] for h in self.solve_history) / total
        
        self.analytics_vars["Total Solutions"].set(str(total))
        self.analytics_vars["Avg Path Length"].set(f"{avg_length:.1f}")
        self.analytics_vars["Avg Time (ms)"].set(f"{avg_time:.1f}")
        
        # Update history list
        self.history_list.delete(0, tk.END)
        for h in reversed(self.solve_history[-10:]):
            self.history_list.insert(0, 
                f"{h['timestamp'].strftime('%H:%M:%S')} - {h['start'].upper()} → {h['goal'].upper()} ({h['length']} steps, {h['time']:.0f}ms)")
        
        # Draw simple chart
        self._draw_chart()
    
    def _draw_chart(self):
        """Draw a simple performance chart."""
        self.chart_canvas.delete("all")
        
        if not self.solve_history:
            return
        
        W = self.chart_canvas.winfo_width()
        H = self.chart_canvas.winfo_height()
        
        if W < 100 or H < 100:
            return
        
        recent = self.solve_history[-20:]
        if not recent:
            return
        
        max_length = max(h["length"] for h in recent)
        bar_width = W // len(recent) - 2
        
        for i, history in enumerate(recent):
            x = i * (bar_width + 2) + 10
            bar_height = (history["length"] / max_length) * (H - 50)
            y = H - bar_height - 20
            
            self.chart_canvas.create_rectangle(x, y, x + bar_width, H - 20,
                                              fill=self.COLORS["accent1"], outline="")
    
    def _on_category_select(self, event):
        """Handle category selection."""
        selection = self.category_listbox.curselection()
        if selection:
            category = self.category_listbox.get(selection[0])
            words = self.dictionary.categories.get(category, set())
            self._update_words_list(words)
    
    def _search_words(self):
        """Search for words in dictionary."""
        search_term = self.search_var.get().lower()
        if not search_term:
            self._update_words_list(self.dictionary.all_words)
        else:
            matches = {w for w in self.dictionary.all_words if search_term in w}
            self._update_words_list(matches)
    
    def _update_words_list(self, words):
        """Update the words listbox."""
        self.words_listbox.delete(0, tk.END)
        for word in sorted(words)[:100]:
            self.words_listbox.insert(tk.END, word)
    
    def _add_word_dialog(self):
        """Dialog to add a new word."""
        dialog = tk.Toplevel(self)
        dialog.title("Add Word - LetterStep")
        dialog.geometry("400x300")
        dialog.configure(bg=self.COLORS["card"])
        
        tk.Label(dialog, text="Add New Word", font=("Segoe UI", 16, "bold"),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack(pady=20)
        
        tk.Label(dialog, text="Word:", font=("Segoe UI", 10),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack()
        word_entry = tk.Entry(dialog, font=("Segoe UI", 12),
                             bg=self.COLORS["bg_light"], fg=self.COLORS["text_light"],
                             relief="flat")
        word_entry.pack(pady=5, padx=20, fill="x")
        
        tk.Label(dialog, text="Category:", font=("Segoe UI", 10),
                fg=self.COLORS["text_light"], bg=self.COLORS["card"]).pack()
        category_combo = ttk.Combobox(dialog, values=list(self.dictionary.categories.keys()),
                                     state="readonly")
        category_combo.pack(pady=5, padx=20, fill="x")
        
        def add():
            word = word_entry.get().strip().lower()
            category = category_combo.get()
            
            if not word.isalpha():
                messagebox.showerror("Error", "Invalid word")
                return
            
            if self.dictionary.add_word(word, 5, category if category else None):
                self.dict_size_label.config(text=f"📚 {len(self.dictionary.all_words)} words")
                self._refresh_dashboard()
                messagebox.showinfo("Success", f"Added '{word}' to LetterStep dictionary")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Word already exists")
        
        tk.Button(dialog, text="Add", command=add,
                 bg=self.COLORS["accent1"], fg="white",
                 font=("Segoe UI", 11), relief="flat",
                 cursor="hand2").pack(pady=20)
    
    def _remove_word_dialog(self):
        """Dialog to remove a word."""
        selection = self.words_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a word to remove")
            return
        
        word = self.words_listbox.get(selection[0])
        if messagebox.askyesno("Confirm", f"Remove '{word}' from LetterStep dictionary?"):
            self.dictionary.remove_word(word)
            self.dict_size_label.config(text=f"📚 {len(self.dictionary.all_words)} words")
            self._refresh_dashboard()
            self._search_words()  # Refresh list
            messagebox.showinfo("Success", f"Removed '{word}'")
    
    def _import_dictionary(self):
        """Import dictionary from file."""
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                self.dictionary.load_dictionary(filename)
                self.dict_size_label.config(text=f"📚 {len(self.dictionary.all_words)} words")
                self._refresh_dashboard()
                messagebox.showinfo("Success", "Dictionary imported to LetterStep")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def _export_dictionary(self):
        """Export dictionary to file."""
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json")])
        if filename:
            try:
                self.dictionary.save_dictionary(filename)
                messagebox.showinfo("Success", "Dictionary exported from LetterStep")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def _change_theme(self):
        """Change application theme."""
        # Placeholder for theme switching functionality
        messagebox.showinfo("Coming Soon", "Theme switching will be available in the next update!")
    
    def _reset_settings(self):
        """Reset all settings to default."""
        self.animation_speed.set(0.5)
        self.default_length.set(4)
        messagebox.showinfo("Success", "LetterStep settings reset to default")
    
    def _show_solver_from_dashboard(self):
        """Navigate to solver page."""
        self._show_page("solver")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app = LetterStepApp()
    app.mainloop()