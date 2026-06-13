"""Cricket knowledge base for the FAQ chatbot."""

FAQS = [
    # Basics
    {
        "question": "What are the rules of cricket?",
        "aliases": [
            "List the rules of cricket",
            "Basic rules of cricket",
            "Main cricket rules explained",
            "Cricket rules for beginners",
            "Tell me cricket rules",
        ],
        "answer": (
            "Key rules of cricket include:\n\n"
            "1. **Teams** — Two sides of 11 players each.\n"
            "2. **Innings** — One team bats while the other bowls and fields.\n"
            "3. **Scoring** — Runs come from running between wickets or hitting boundaries (4 or 6).\n"
            "4. **Overs** — A legal over has six deliveries from one bowler.\n"
            "5. **Dismissals** — Batters can be out bowled, caught, LBW, run out, stumped, and more.\n"
            "6. **Formats** — Tests, ODIs, and T20s have different overs/day limits.\n"
            "7. **Winning** — The team with the higher score wins (super overs or other tie-breaks may apply).\n"
            "8. **Umpires** — On-field officials enforce rules; DRS can review close decisions."
        ),
    },
    {
        "question": "What is cricket?",
        "aliases": [
            "Explain cricket to me",
            "Define cricket",
            "Tell me about cricket sport",
        ],
        "answer": (
            "Cricket is a bat-and-ball sport played between two teams of eleven players. "
            "One team bats to score runs while the other bowls and fields to restrict scoring and dismiss batters."
        ),
    },
    {
        "question": "How many players are there in a cricket team?",
        "answer": "Each cricket team fields eleven players at a time, including batters, bowlers, wicketkeepers, and all-rounders.",
    },
    {
        "question": "What is the objective of cricket?",
        "answer": (
            "The batting side tries to score as many runs as possible, while the bowling side tries to "
            "take wickets and limit runs. The team with the higher score wins, subject to format rules."
        ),
    },
    {
        "question": "What is a run in cricket?",
        "answer": (
            "A run is the basic unit of scoring. Batters earn runs by running between the wickets after hitting "
            "the ball, or automatically from boundaries and extras."
        ),
    },
    {
        "question": "What is a wicket in cricket?",
        "answer": (
            "A wicket can mean the set of three stumps, the pitch area, or a dismissal. "
            "When a batter is out, the fielding team takes a wicket."
        ),
    },
    {
        "question": "What is the pitch in cricket?",
        "answer": (
            "The pitch is the 22-yard strip in the center of the ground where most bowling and batting action happens. "
            "Its condition strongly affects bounce, spin, and pace."
        ),
    },
    {
        "question": "What are stumps and bails?",
        "answer": (
            "Stumps are three vertical posts at each end of the pitch. Bails are the two small pieces resting on top. "
            "If the bails are dislodged legally, the batter can be out bowled, stumped, or run out."
        ),
    },
    {
        "question": "What is the crease in cricket?",
        "answer": (
            "The crease is a marked line near the stumps. Batters must stay grounded behind the popping crease "
            "to avoid being stumped or run out."
        ),
    },
    # Formats
    {
        "question": "What are the main formats of cricket?",
        "answer": (
            "The three main international formats are Test cricket, One Day Internationals (ODIs), "
            "and Twenty20 (T20). Tests last up to five days, ODIs 50 overs per side, and T20s 20 overs per side."
        ),
    },
    {
        "question": "What is Test cricket?",
        "answer": (
            "Test cricket is the longest format, played over five days with two innings per team in most cases. "
            "It is considered the most traditional and demanding form of the game."
        ),
    },
    {
        "question": "What is an ODI in cricket?",
        "answer": (
            "An ODI (One Day International) is a limited-overs match where each team usually faces 50 overs. "
            "The game is completed in one day, unlike Test cricket."
        ),
    },
    {
        "question": "What is T20 cricket?",
        "answer": (
            "T20 cricket gives each team 20 overs. It is the shortest mainstream format and emphasizes aggressive batting, "
            "innovative shots, and fast results."
        ),
    },
    {
        "question": "What is an over in cricket?",
        "answer": (
            "An over consists of six legal deliveries bowled by one bowler from one end. "
            "After six balls, a new over begins, often with a different bowler from the other end."
        ),
    },
    {
        "question": "What is a powerplay in cricket?",
        "answer": (
            "A powerplay is a phase in limited-overs cricket with fielding restrictions, allowing fewer fielders outside "
            "the inner circle. This encourages aggressive batting early in the innings."
        ),
    },
    {
        "question": "What is a super over?",
        "answer": (
            "A super over is a tie-breaker in some T20 and ODI matches. Each team faces one over, "
            "and the side scoring more runs wins. Wickets lost can matter depending on tournament rules."
        ),
    },
    # Batting
    {
        "question": "What is a century in cricket?",
        "answer": (
            "A century is when a batter scores 100 or more runs in a single innings. "
            "It is a major milestone and a sign of batting excellence."
        ),
    },
    {
        "question": "What is a double century in cricket?",
        "answer": (
            "A double century means a batter has scored 200 or more runs in one innings. "
            "It is rare and usually seen in Tests and occasionally in ODIs."
        ),
    },
    {
        "question": "What is a duck in cricket?",
        "answer": (
            "A duck is when a batter is dismissed without scoring any runs. "
            "A golden duck means getting out on the first ball faced."
        ),
    },
    {
        "question": "What is a boundary in cricket?",
        "answer": (
            "If the ball crosses the boundary after touching the ground, it is four runs. "
            "If it crosses without touching the ground, it is six runs."
        ),
    },
    {
        "question": "What is the difference between a four and a six?",
        "answer": (
            "A four is scored when the ball reaches the boundary after bouncing at least once. "
            "A six is scored when the ball clears the boundary on the full without bouncing."
        ),
    },
    {
        "question": "What is strike rate in batting?",
        "answer": (
            "Batting strike rate shows how quickly a batter scores, usually runs per 100 balls. "
            "It is especially important in T20 and ODI cricket."
        ),
    },
    {
        "question": "What is a nightwatchman in Test cricket?",
        "answer": (
            "A nightwatchman is a lower-order batter sent in near the end of a day's play to protect a specialist batter "
            "from facing difficult conditions in the final overs."
        ),
    },
    {
        "question": "What is a follow-on in Test cricket?",
        "answer": (
            "A follow-on happens when the team batting second trails by a large margin after the first innings. "
            "The captain may enforce it, making the trailing team bat again immediately."
        ),
    },
    # Bowling
    {
        "question": "What is a no-ball in cricket?",
        "answer": (
            "A no-ball is an illegal delivery, often due to overstepping the crease or an illegal bowling action. "
            "The batting team gets one run and usually a free hit in limited-overs cricket."
        ),
    },
    {
        "question": "What is a wide ball in cricket?",
        "answer": (
            "A wide is called when the delivery is too far from the batter to play normally. "
            "The batting side gets an extra run, and the ball must be bowled again."
        ),
    },
    {
        "question": "What is a yorker in cricket?",
        "answer": (
            "A yorker is a delivery aimed at the batter's feet or the base of the stumps. "
            "It is effective in death overs because it is hard to hit for boundaries."
        ),
    },
    {
        "question": "What is a bouncer in cricket?",
        "answer": (
            "A bouncer is a short-pitched delivery that rises toward the batter's upper body or head. "
            "Bowlers use it to intimidate or force defensive shots."
        ),
    },
    {
        "question": "What is swing bowling?",
        "answer": (
            "Swing bowling is when the ball moves sideways through the air, usually with a newer ball. "
            "Outswing moves away from the batter; inswing moves toward them."
        ),
    },
    {
        "question": "What is reverse swing?",
        "answer": (
            "Reverse swing happens with an older ball, often when one side is rough and the other shiny. "
            "The ball swings in the opposite direction to conventional swing."
        ),
    },
    {
        "question": "What is spin bowling?",
        "answer": (
            "Spin bowlers use finger or wrist action to turn the ball after pitching. "
            "Off-spin turns into the right-handed batter; leg-spin turns away."
        ),
    },
    {
        "question": "What is a hat-trick in cricket?",
        "answer": (
            "A hat-trick is when a bowler dismisses three batters with three consecutive legal deliveries. "
            "It is one of the rarest and most celebrated bowling achievements."
        ),
    },
    {
        "question": "What is economy rate in bowling?",
        "answer": (
            "Economy rate measures how many runs a bowler concedes per over. "
            "Lower economy rates are especially valuable in limited-overs cricket."
        ),
    },
    # Dismissals
    {
        "question": "How can a batter get out in cricket?",
        "answer": (
            "Common dismissals include bowled, caught, lbw, run out, stumped, hit wicket, "
            "handled the ball, obstructing the field, timed out, and hit the ball twice."
        ),
    },
    {
        "question": "What is LBW or leg before wicket in cricket?",
        "answer": (
            "LBW stands for leg before wicket. A batter can be out if the ball would have hit the stumps "
            "but is blocked by the body instead, subject to several conditions."
        ),
    },
    {
        "question": "What is a catch out in cricket?",
        "answer": (
            "A batter is caught out when a fielder catches the ball on the full after it touches the bat or glove. "
            "It is one of the most common dismissals."
        ),
    },
    {
        "question": "What is run out in cricket?",
        "answer": (
            "A run out happens when fielders break the stumps with the ball before the batter completes a run "
            "and is inside the crease."
        ),
    },
    {
        "question": "What is stumped in cricket?",
        "answer": (
            "Stumped occurs when the wicketkeeper removes the bails while the batter is out of the crease "
            "and not attempting a run, usually against spin bowlers."
        ),
    },
    # Fielding & roles
    {
        "question": "What does a wicketkeeper do?",
        "answer": (
            "The wicketkeeper stands behind the stumps and catches edges, effects stumpings, "
            "and supports the bowlers by keeping pressure on batters."
        ),
    },
    {
        "question": "What is an all-rounder in cricket?",
        "answer": (
            "An all-rounder contributes significantly with both bat and ball. "
            "Examples include players who can score runs and take wickets regularly."
        ),
    },
    {
        "question": "What is a slip fielder?",
        "answer": (
            "Slip fielders stand close behind the batter on the off side, usually to catch edges from fast or swing bowlers. "
            "There can be multiple slips in attacking fields."
        ),
    },
    {
        "question": "What is a captain's role in cricket?",
        "answer": (
            "The captain sets fields, chooses bowlers, makes tactical decisions, and represents the team on the field. "
            "Leadership and game reading are crucial parts of the role."
        ),
    },
    # Umpiring & technology
    {
        "question": "What is DRS in cricket?",
        "answer": (
            "DRS (Decision Review System) lets teams challenge on-field umpire decisions using technology "
            "such as ball tracking, UltraEdge, and replays. Teams have a limited number of reviews."
        ),
    },
    {
        "question": "What is the third umpire in cricket?",
        "answer": (
            "The third umpire reviews close decisions using TV replays, including run outs, stumpings, "
            "boundary checks, and DRS referrals."
        ),
    },
    {
        "question": "What is ball tracking in cricket?",
        "answer": (
            "Ball tracking predicts the path of the ball after pitching. "
            "It is used mainly for LBW reviews under the DRS system."
        ),
    },
    # IPL & leagues
    {
        "question": "What is the Indian Premier League IPL?",
        "answer": (
            "The Indian Premier League (IPL) is a major T20 franchise league held annually in India. "
            "It features top international and domestic players, large crowds, and high-intensity matches."
        ),
    },
    {
        "question": "How does the IPL auction work?",
        "answer": (
            "Franchises bid for players in an auction before the season. "
            "Each team has a purse and squad limits, and players are bought based on base price and bidding demand."
        ),
    },
    {
        "question": "Which teams play in the IPL?",
        "answer": (
            "IPL franchises include teams such as Mumbai Indians, Chennai Super Kings, Royal Challengers Bengaluru, "
            "Kolkata Knight Riders, Delhi Capitals, Rajasthan Royals, Sunrisers Hyderabad, and Punjab Kings."
        ),
    },
    {
        "question": "What is the Big Bash League?",
        "answer": (
            "The Big Bash League (BBL) is Australia's popular T20 franchise competition, "
            "known for entertaining cricket and strong local fan support."
        ),
    },
    {
        "question": "What is The Hundred?",
        "answer": (
            "The Hundred is a 100-ball franchise competition in England. "
            "It uses a different scoring structure and has helped attract new audiences to cricket."
        ),
    },
    # International cricket
    {
        "question": "What is the Cricket World Cup?",
        "answer": (
            "The ICC Cricket World Cup is the premier ODI tournament, usually held every four years. "
            "National teams compete for the title over several weeks."
        ),
    },
    {
        "question": "What is the T20 World Cup?",
        "answer": (
            "The ICC T20 World Cup is the global championship for the shortest international format. "
            "It features fast-paced matches and often produces surprise results."
        ),
    },
    {
        "question": "What is the Ashes series?",
        "answer": (
            "The Ashes is a famous Test series between England and Australia. "
            "It is one of cricket's oldest and most intense rivalries."
        ),
    },
    {
        "question": "What is the ICC ranking system?",
        "answer": (
            "The ICC ranks teams and players in Tests, ODIs, and T20s based on recent performances. "
            "Ratings change after every match and help compare form across nations."
        ),
    },
    # Indian cricket
    {
        "question": "Who is the captain of India in cricket?",
        "answer": (
            "India's captain varies by format and changes over time. "
            "For the latest captain in Tests, ODIs, or T20Is, check recent ICC or BCCI announcements."
        ),
    },
    {
        "question": "What is the BCCI?",
        "answer": (
            "The BCCI (Board of Control for Cricket in India) governs cricket in India, "
            "including the national team, domestic competitions, and the IPL."
        ),
    },
    {
        "question": "What is Ranji Trophy?",
        "answer": (
            "The Ranji Trophy is India's premier first-class domestic cricket competition. "
            "Many Indian Test players develop through this tournament."
        ),
    },
    # Legends & records
    {
        "question": "Who is Sachin Tendulkar?",
        "answer": (
            "Sachin Tendulkar is one of cricket's greatest batters, known for records such as 100 international centuries "
            "and a long career representing India from 1989 to 2013."
        ),
    },
    {
        "question": "Who is Virat Kohli?",
        "answer": (
            "Virat Kohli is a modern great known for aggressive batting, consistency across formats, "
            "and leading India to many notable wins as captain."
        ),
    },
    {
        "question": "Who is MS Dhoni or Mahendra Singh Dhoni?",
        "answer": (
            "MS Dhoni is a legendary wicketkeeper-batter and captain, famous for calm finishing, "
            "sharp tactical decisions, and leading India to major ICC titles."
        ),
    },
    {
        "question": "Who has the most runs in international cricket?",
        "answer": (
            "Sachin Tendulkar holds the record for most runs in international cricket across Tests and ODIs. "
            "Record lists are updated as active players continue their careers."
        ),
    },
    {
        "question": "Who has the most wickets in international cricket?",
        "answer": (
            "Muttiah Muralitharan holds the record for most wickets in international cricket. "
            "His off-spin made him especially dominant in Tests and ODIs."
        ),
    },
    {
        "question": "What is the highest individual score in ODI cricket?",
        "answer": (
            "Rohit Sharma has scored 264, the highest individual score in ODI cricket. "
            "Such innings are rare and require long batting periods in limited overs."
        ),
    },
    # Terminology
    {
        "question": "What is a googly in cricket?",
        "answer": (
            "A googly is a leg-spinner's delivery that turns the opposite way to a normal leg-break, "
            "often deceiving batters expecting spin toward the leg side."
        ),
    },
    {
        "question": "What is a doosra in cricket?",
        "answer": (
            "A doosra is an off-spinner's delivery that turns away from the right-handed batter, "
            "the opposite direction of a normal off-break."
        ),
    },
    {
        "question": "What is a maiden over?",
        "answer": (
            "A maiden over is an over in which no runs are scored from the bat, though byes or leg byes may still occur. "
            "It is a sign of strong bowling control."
        ),
    },
    {
        "question": "What is a free hit in cricket?",
        "answer": (
            "After a no-ball in limited-overs cricket, the next delivery is a free hit. "
            "The batter can be dismissed only by run out, hit the ball twice, obstructing the field, or handled the ball."
        ),
    },
    {
        "question": "What is a leg bye in cricket?",
        "answer": (
            "Leg byes are runs scored when the ball hits the batter's body and they complete runs, "
            "provided they attempted a shot or tried to avoid being hit."
        ),
    },
    {
        "question": "What is a bye in cricket?",
        "answer": (
            "Byes are runs scored when the ball passes the batter and wicketkeeper without contact, "
            "and the batters run. They count as extras."
        ),
    },
    {
        "question": "What is extras in cricket?",
        "answer": (
            "Extras are runs not scored off the bat, including wides, no-balls, byes, and leg byes. "
            "They are added to the team total."
        ),
    },
    {
        "question": "What are death overs in T20 cricket?",
        "answer": (
            "Death overs usually refer to the final overs of an innings, often overs 16 to 20 in T20 cricket. "
            "Batters attack aggressively and bowlers use yorkers and slower balls."
        ),
    },
    {
        "question": "What is a finisher in cricket?",
        "answer": (
            "A finisher is a batter skilled at scoring quickly at the end of an innings, "
            "often chasing targets under pressure in T20s and ODIs."
        ),
    },
    {
        "question": "What is a pinch hitter in cricket?",
        "answer": (
            "A pinch hitter is a batter promoted up the order temporarily to attack aggressively, "
            "usually to disrupt bowling plans in limited-overs cricket."
        ),
    },
    # Equipment & conditions
    {
        "question": "What bat is used in cricket?",
        "answer": (
            "Cricket bats are flat on one side and made mainly from willow. "
            "Players choose bat weight and balance based on style and format."
        ),
    },
    {
        "question": "What ball is used in cricket?",
        "answer": (
            "A cricket ball is hard, cork-centered, and leather-covered. "
            "Red balls are common in Tests, while white balls are used in most limited-overs day/night games."
        ),
    },
    {
        "question": "Why does the ball swing more in England?",
        "answer": (
            "Swing often increases in cloudy, humid conditions, which are common in England. "
            "A newer ball and skilled seam presentation also help bowlers move the ball."
        ),
    },
    {
        "question": "What is a green pitch in cricket?",
        "answer": (
            "A green pitch has more grass and usually assists seam bowlers early with bounce and movement. "
            "Batters may struggle until the surface flattens."
        ),
    },
    {
        "question": "What is a turning track in cricket?",
        "answer": (
            "A turning track helps spin bowlers because the ball grips and deviates sharply after pitching. "
            "Such surfaces are common in the subcontinent."
        ),
    },
    # How the bot works
    {
        "question": "How does this cricket chatbot work?",
        "answer": (
            "Your question is cleaned and tokenized with NLTK, converted into TF-IDF vectors, "
            "and matched against cricket FAQ entries using cosine similarity. "
            "The closest match above a confidence threshold is returned."
        ),
    },
]

SUGGESTED_QUESTIONS = [
    "List the rules of cricket",
    "What is LBW in cricket?",
    "What is a hat-trick?",
    "Who is Sachin Tendulkar?",
    "What is DRS in cricket?",
]
