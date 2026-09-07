# -*- coding: utf-8 -*-
# key = exact English source string as it appears in a text node / attribute
T = {

# ---------- gate / nav / hero ----------
"Network & Security": ("الشبكات والأمن","Réseaux & Sécurité"),
"Welcome to my website": ("مرحباً بك في موقعي","Bienvenue sur mon site"),
"About": ("نبذة","À propos"),
"Focus": ("التخصص","Expertise"),
"Experience": ("الخبرة","Expérience"),
"Services": ("الخدمات","Services"),
"Project": ("المشروع","Projet"),
"Contact": ("تواصل","Contact"),
"Available for work": ("متاح للعمل","Disponible"),
"AI Integrated": ("مدعوم بالذكاء الاصطناعي","IA intégrée"),
"Explore my work": ("استكشف أعمالي","Découvrir mon travail"),
"Scroll": ("مرّر للأسفل","Défiler"),

# typed words
"Network Admin": ("مدير شبكات","Admin Réseau"),
"Security Specialist": ("أخصائي أمن","Spécialiste Sécurité"),
"VLAN Architect": ("مهندس VLAN","Architecte VLAN"),
"Firewall Engineer": ("مهندس جدار حماية","Ingénieur Pare-feu"),

# ---------- 01 about ----------
"01 — About": ("٠١ — نبذة عني","01 — À propos"),
"Networks that stay up.": ("شبكات لا تتوقّف.","Des réseaux qui tiennent."),
"Data that stays private.": ("وبيانات تبقى محميّة.","Des données qui restent privées."),
"I'm": ("أنا","Je suis"),
"— a specialist in": ("— مختص في","— spécialiste en"),
"Information Network Administration and Security": ("إدارة وأمن شبكات المعلومات","Administration et Sécurité des Réseaux Informatiques"),
", holding a university degree in the field. I design, deploy and defend the infrastructure that small businesses, offices and institutions run on: structured LANs, segmented VLANs, hardened firewalls, controlled access and monitored traffic.":
 ("، حاصل على شهادة جامعية في هذا المجال. أُصمّم وأنشر وأحمي البنية التحتية التي تعتمد عليها الشركات الصغيرة والمكاتب والمؤسسات: شبكات محلية منظّمة، وشبكات VLAN مقسّمة، وجدران حماية محصّنة، ووصول مضبوط، وحركة مرور تحت المراقبة.",
  ", titulaire d'un diplôme universitaire dans le domaine. Je conçois, déploie et protège l'infrastructure sur laquelle reposent les petites entreprises, les bureaux et les institutions : réseaux locaux structurés, VLAN segmentés, pare-feu durcis, accès contrôlé et trafic supervisé."),
"My approach is simple: build it clean, document it clearly, secure it by default. A network should be invisible when it works — and understandable when it doesn't. I pair solid fundamentals in routing, switching and defense-in-depth with modern":
 ("منهجي بسيط: بناء نظيف، توثيق واضح، وأمان افتراضي. الشبكة يجب أن تكون غير مرئية حين تعمل — ومفهومة حين تتعطّل. أجمع بين أسس متينة في التوجيه والتبديل والدفاع المتعدد الطبقات وبين",
  "Mon approche est simple : construire proprement, documenter clairement, sécuriser par défaut. Un réseau doit être invisible quand il fonctionne — et compréhensible quand il tombe. J'associe des fondamentaux solides en routage, commutation et défense en profondeur à des"),
"AI-assisted tooling": ("أدوات مدعومة بالذكاء الاصطناعي","outils assistés par IA"),
"that speeds up diagnostics and hardening, while every decision still passes through human judgment.":
 ("تُسرّع التشخيص والتحصين، مع بقاء كل قرار خاضعاً للحكم البشري.",
  "modernes qui accélèrent le diagnostic et le durcissement, chaque décision restant soumise au jugement humain."),
"Uptime mindset": ("عقلية الاستمرارية","Culture de la disponibilité"),
"Layers secured": ("طبقات مؤمَّنة","Couches sécurisées"),
"Assisted workflow": ("سير عمل مُعان","Flux assisté"),
"Human reviewed": ("مراجَع بشرياً","Revu par un humain"),

# ---------- 02 focus ----------
"02 — Technical Focus": ("٠٢ — التخصص التقني","02 — Expertise technique"),
"What I work on": ("مجالات عملي","Mes domaines"),
"The core disciplines behind every deployment I deliver.":
 ("التخصصات الأساسية وراء كل عملية نشر أُنجزها.","Les disciplines clés derrière chaque déploiement que je livre."),

"Network Infrastructure": ("البنية التحتية للشبكات","Infrastructure réseau"),
"LAN/WAN design, structured cabling logic, switching, routing, VLAN segmentation, subnetting and IP addressing plans built to scale.":
 ("تصميم شبكات LAN/WAN، ومنطق الكبلات المهيكلة، والتبديل، والتوجيه، وتقسيم VLAN، وتقسيم الشبكات الفرعية، وخطط عنونة IP قابلة للتوسّع.",
  "Conception LAN/WAN, câblage structuré, commutation, routage, segmentation VLAN, sous-réseaux et plans d'adressage IP évolutifs."),
"Security & Hardening": ("الأمن والتحصين","Sécurité & Durcissement"),
"Firewall policy, ACLs, port security, NAT, VPN tunnels, WPA2/3 enterprise wireless, password and privilege management, patch discipline.":
 ("سياسات جدار الحماية، وقوائم التحكم بالوصول، وأمن المنافذ، وNAT، وأنفاق VPN، وشبكات WPA2/3 المؤسسية، وإدارة كلمات المرور والصلاحيات، وانضباط التحديثات.",
  "Politiques pare-feu, ACL, port security, NAT, tunnels VPN, Wi-Fi entreprise WPA2/3, gestion des mots de passe et privilèges, discipline des correctifs."),
"System Administration": ("إدارة الأنظمة","Administration système"),
"Windows & Linux server roles, Active Directory, DHCP/DNS, file and print services, user provisioning, GPO and access control.":
 ("أدوار خوادم Windows و Linux، وActive Directory، وDHCP/DNS، وخدمات الملفات والطباعة، وإنشاء المستخدمين، وسياسات GPO والتحكم بالوصول.",
  "Rôles serveurs Windows & Linux, Active Directory, DHCP/DNS, services de fichiers et d'impression, gestion des comptes, GPO et contrôle d'accès."),
"Monitoring & Diagnostics": ("المراقبة والتشخيص","Supervision & Diagnostic"),
"Traffic analysis with Wireshark and Zabbix, packet-level troubleshooting, SNMP and Syslog review, latency and bottleneck hunting.":
 ("تحليل حركة المرور عبر Wireshark وZabbix، واستكشاف الأعطال على مستوى الحزم، ومراجعة SNMP وSyslog، وتتبّع زمن الاستجابة والاختناقات.",
  "Analyse du trafic avec Wireshark et Zabbix, dépannage au niveau paquet, revue SNMP et Syslog, chasse à la latence et aux goulots d'étranglement."),
"Simulation & Labs": ("المحاكاة والمختبرات","Simulation & Laboratoires"),
"Full topology prototyping in Cisco Packet Tracer and GNS3, virtualized test benches, configuration validation before production.":
 ("نمذجة كاملة للطوبولوجيا في Cisco Packet Tracer وGNS3، ومنصات اختبار افتراضية، والتحقق من الإعدادات قبل الإنتاج.",
  "Prototypage complet de topologies sous Cisco Packet Tracer et GNS3, bancs de test virtualisés, validation des configurations avant production."),
"Backup & Continuity": ("النسخ الاحتياطي والاستمرارية","Sauvegarde & Continuité"),
"Backup strategies, redundancy and failover paths, recovery procedures, and disaster-recovery planning that's actually been tested.":
 ("استراتيجيات النسخ الاحتياطي، ومسارات التكرار والتحويل عند العطل، وإجراءات الاستعادة، وخطط التعافي من الكوارث المُختبرة فعلياً.",
  "Stratégies de sauvegarde, redondance et chemins de bascule, procédures de restauration et plan de reprise réellement testé."),
"Web Design & Development": ("تصميم وتطوير المواقع","Conception & Développement Web"),
"Commercial websites built from scratch: responsive layouts, clean lightweight code, performance tuning, hosting setup and full handover.":
 ("مواقع تجارية مبنية من الصفر: تخطيطات متجاوبة، وشيفرة نظيفة وخفيفة، وضبط الأداء، وإعداد الاستضافة، وتسليم كامل.",
  "Sites commerciaux créés de zéro : mises en page responsives, code léger et propre, optimisation des performances, hébergement et livraison complète."),

# ---------- 03 experience ----------
"03 — Experience": ("٠٣ — الخبرة المهنية","03 — Expérience"),
"Where I've worked": ("أين عملت","Mon parcours"),
"Field engineering, operational responsibility and commercial web work — beyond the lab.":
 ("هندسة ميدانية، ومسؤولية تشغيلية، وأعمال ويب تجارية — خارج حدود المختبر.",
  "Ingénierie de terrain, responsabilité opérationnelle et travail web commercial — au-delà du laboratoire."),
"Freelance · Ongoing": ("عمل حر · مستمر","Freelance · En cours"),
"Designing and building websites of all kinds — commercial, personal and institutional — from concept to deployment.":
 ("تصميم وبناء مواقع بجميع أنواعها — تجارية وشخصية ومؤسسية — من الفكرة حتى النشر.",
  "Conception et réalisation de sites de tous types — commerciaux, personnels et institutionnels — du concept au déploiement."),
"Business sites, landing pages, portfolios, storefronts and personal pages":
 ("مواقع أعمال، وصفحات هبوط، ومعارض أعمال، ومتاجر، وصفحات شخصية",
  "Sites d'entreprise, landing pages, portfolios, boutiques et pages personnelles"),
"Responsive layouts that work cleanly on desktop, tablet and mobile":
 ("تخطيطات متجاوبة تعمل بسلاسة على الحاسوب واللوحي والهاتف",
  "Mises en page responsives sur ordinateur, tablette et mobile"),
"Performance-first builds — fast loading, lightweight, and search-engine friendly":
 ("بناء يضع الأداء أولاً — تحميل سريع، وخفّة، وتوافق مع محركات البحث",
  "Priorité à la performance — chargement rapide, léger et optimisé pour le référencement"),
"Full delivery: design, development, hosting setup and handover":
 ("تسليم متكامل: التصميم، والتطوير، وإعداد الاستضافة، والتسليم النهائي",
  "Livraison complète : design, développement, hébergement et remise du projet"),
"Responsive Design": ("تصميم متجاوب","Design responsive"),
"Performance": ("الأداء","Performance"),
"Deployment": ("النشر","Déploiement"),

"Field Test Engineer — CTE": ("مهندس اختبار ميداني — CTE","Ingénieur d'essais terrain — CTE"),
"Algérie Télécom — CTE Department · 6 months": ("اتصالات الجزائر — قسم CTE · ٦ أشهر","Algérie Télécom — Département CTE · 6 mois"),
"CTE department (Centre de Transmission / Technical Operations) — on-site testing and validation of telecom infrastructure.":
 ("قسم CTE (مركز الإرسال / العمليات التقنية) — اختبار والتحقق الميداني من البنية التحتية للاتصالات.",
  "Département CTE (Centre de Transmission / Opérations Techniques) — tests et validation sur site de l'infrastructure télécom."),
"Field testing of network lines and subscriber connections across live sites":
 ("اختبار ميداني لخطوط الشبكة ووصلات المشتركين في مواقع تشغيلية حيّة",
  "Tests terrain des lignes réseau et des raccordements abonnés sur sites en exploitation"),
"Fault diagnosis, signal quality measurement and connectivity verification":
 ("تشخيص الأعطال، وقياس جودة الإشارة، والتحقق من الاتصال",
  "Diagnostic de pannes, mesure de la qualité du signal et vérification de la connectivité"),
"Documenting test results and reporting anomalies to technical teams":
 ("توثيق نتائج الاختبارات ورفع تقارير الأعطال إلى الفرق التقنية",
  "Documentation des résultats et remontée des anomalies aux équipes techniques"),
"Working inside the CTE unit of the regional Algérie Télécom directorate":
 ("العمل داخل وحدة CTE التابعة للمديرية الجهوية لاتصالات الجزائر",
  "Intégration à l'unité CTE de la direction régionale d'Algérie Télécom"),
"Hands-on exposure to real operator-grade infrastructure and procedures":
 ("احتكاك مباشر ببنية تحتية وإجراءات بمستوى المشغّلين الحقيقيين",
  "Expérience directe d'une infrastructure et de procédures de niveau opérateur"),
"Field Testing": ("اختبار ميداني","Tests terrain"),
"Fault Diagnosis": ("تشخيص الأعطال","Diagnostic de pannes"),
"Telecom Lines": ("خطوط الاتصالات","Lignes télécom"),
"Reporting": ("إعداد التقارير","Reporting"),

"Storage & Inventory Manager": ("مسؤول المخزون والتخزين","Responsable Stock & Inventaire"),
"Ardis — Auchan Group · Largest mall in the country": ("أرديس — مجموعة أوشان · أكبر مركز تجاري في البلاد","Ardis — Groupe Auchan · Plus grand centre commercial du pays"),
"Responsible for warehouse operations at a high-volume retail site.":
 ("مسؤول عن عمليات المستودع في موقع بيع بالتجزئة عالي الحركة.",
  "Responsable des opérations d'entrepôt sur un site de vente à fort volume."),
"Managing stock intake, storage organisation and outbound flow at scale":
 ("إدارة استلام البضائع، وتنظيم التخزين، وتدفّق الإخراج على نطاق واسع",
  "Gestion des réceptions, de l'organisation du stockage et des flux sortants à grande échelle"),
"Inventory accuracy, stock-level tracking and discrepancy resolution":
 ("دقّة الجرد، وتتبّع مستويات المخزون، ومعالجة الفروقات",
  "Exactitude des inventaires, suivi des niveaux de stock et traitement des écarts"),
"Coordinating with suppliers and internal departments under daily pressure":
 ("التنسيق مع الموردين والأقسام الداخلية تحت ضغط يومي",
  "Coordination avec les fournisseurs et les services internes sous pression quotidienne"),
"Applying structure and traceability — the same discipline I bring to networks":
 ("تطبيق التنظيم وقابلية التتبّع — الانضباط نفسه الذي أطبّقه على الشبكات",
  "Structure et traçabilité — la même rigueur que j'applique aux réseaux"),
"Inventory Control": ("مراقبة المخزون","Gestion des stocks"),
"Logistics": ("اللوجستيك","Logistique"),
"Team Coordination": ("تنسيق الفريق","Coordination d'équipe"),
"Process Discipline": ("انضباط الإجراءات","Rigueur des процédures".replace("проц","proc")),

# ---------- 04 services ----------
"04 — Services": ("٠٤ — الخدمات","04 — Services"),
"IT services I offer": ("الخدمات التي أقدّمها","Les services que je propose"),
"Practical, end-to-end support — from the first cable to the last audit line.":
 ("دعم عملي متكامل — من أول كبل إلى آخر سطر في تقرير التدقيق.",
  "Un accompagnement complet et concret — du premier câble à la dernière ligne d'audit."),
"Network Setup & Configuration": ("تركيب وتهيئة الشبكات","Installation & Configuration réseau"),
"Complete build-out for offices, labs, shops and homes: router and switch configuration, VLANs, Wi-Fi coverage, guest isolation, and clean IP planning with full documentation handed over.":
 ("إنشاء كامل للمكاتب والمخابر والمحلات والمنازل: تهيئة الموجّهات والمبدّلات، وشبكات VLAN، وتغطية Wi-Fi، وعزل الضيوف، وتخطيط IP نظيف مع توثيق كامل عند التسليم.",
  "Déploiement complet pour bureaux, laboratoires, commerces et domiciles : configuration routeurs et switchs, VLAN, couverture Wi-Fi, isolation invités et plan d'adressage IP propre, documentation remise."),
"Security Audit & Hardening": ("تدقيق أمني وتحصين","Audit de sécurité & Durcissement"),
"Assessment of your current setup, exposure review, firewall and access-control tuning, credential hygiene, and a prioritized remediation report written in plain language.":
 ("تقييم لوضعك الحالي، ومراجعة نقاط الانكشاف، وضبط جدار الحماية والتحكم بالوصول، وتنظيم بيانات الاعتماد، وتقرير معالجة مرتّب حسب الأولوية بلغة واضحة.",
  "Évaluation de votre installation, revue des expositions, réglage du pare-feu et des contrôles d'accès, hygiène des identifiants et rapport de remédiation priorisé en langage clair."),
"Server & User Management": ("إدارة الخوادم والمستخدمين","Gestion serveurs & utilisateurs"),
"Domain controllers, Active Directory, shared storage, permissions matrices, DHCP/DNS services, and onboarding/offboarding procedures that don't leave doors open.":
 ("وحدات تحكم النطاق، وActive Directory، والتخزين المشترك، ومصفوفات الصلاحيات، وخدمات DHCP/DNS، وإجراءات ضمّ ومغادرة الموظفين دون ترك أبواب مفتوحة.",
  "Contrôleurs de domaine, Active Directory, stockage partagé, matrices de droits, services DHCP/DNS et procédures d'arrivée/départ qui ne laissent aucune porte ouverte."),
"Troubleshooting & Maintenance": ("استكشاف الأعطال والصيانة","Dépannage & Maintenance"),
"Fast diagnosis of connectivity, performance and configuration failures, plus scheduled maintenance, updates and health checks to stop problems before they start.":
 ("تشخيص سريع لأعطال الاتصال والأداء والإعدادات، إضافة إلى صيانة دورية وتحديثات وفحوص سلامة توقف المشاكل قبل وقوعها.",
  "Diagnostic rapide des pannes de connectivité, de performance et de configuration, plus maintenance planifiée, mises à jour et contrôles de santé pour prévenir les incidents."),
"Backup & Recovery Planning": ("تخطيط النسخ الاحتياطي والاستعادة","Plan de sauvegarde & restauration"),
"Designing what gets backed up, how often, where it lives, and how quickly it comes back. Includes restore drills, because an untested backup isn't a backup.":
 ("تحديد ما يُنسخ احتياطياً، وكم مرة، وأين يُخزَّن، وبأي سرعة يُستعاد. مع تمارين استعادة فعلية، لأن نسخة غير مُختبرة ليست نسخة.",
  "Définir ce qui est sauvegardé, à quelle fréquence, où et à quelle vitesse c'est restauré. Avec des exercices de restauration, car une sauvegarde non testée n'en est pas une."),
"Technical Consulting & Training": ("استشارات وتدريب تقني","Conseil & Formation technique"),
"Equipment selection, upgrade roadmaps, cost-aware architecture advice, and hands-on training so your team can operate the system with confidence.":
 ("اختيار المعدات، وخرائط طريق الترقية، ومشورة معمارية واعية بالتكلفة، وتدريب عملي يمكّن فريقك من تشغيل النظام بثقة.",
  "Choix des équipements, feuilles de route d'évolution, conseils d'architecture au juste coût et formation pratique pour que votre équipe pilote le système en confiance."),
"Business Website Creation": ("إنشاء مواقع للأعمال","Création de sites professionnels"),
"Design and build of commercial sites for shops, offices and professionals — responsive, fast, SEO-aware, deployed and handed over ready to use.":
 ("تصميم وبناء مواقع تجارية للمحلات والمكاتب والمهنيين — متجاوبة وسريعة ومهيّأة لمحركات البحث، منشورة ومسلَّمة جاهزة للاستخدام.",
  "Conception et réalisation de sites commerciaux pour commerces, bureaux et professionnels — responsives, rapides, optimisés SEO, déployés et prêts à l'emploi."),

# ---------- 05 AI ----------
"05 — Innovation": ("٠٥ — الابتكار","05 — Innovation"),
"AI in the workflow.": ("الذكاء الاصطناعي في صميم العمل.","L'IA dans le flux de travail."),
"Judgment stays human.": ("والقرار يبقى بشرياً.","Le jugement reste humain."),
"Technology moves fast, and standing still is its own kind of vulnerability. I integrate":
 ("التقنية تتقدّم بسرعة، والجمود في حدّ ذاته ثغرة. أدمج",
  "La technologie avance vite, et l'immobilisme est en soi une vulnérabilité. J'intègre"),
"artificial intelligence": ("الذكاء الاصطناعي","l'intelligence artificielle"),
"into my daily work to move faster and see more — while keeping the responsibility, the ethics and the final call firmly in human hands.":
 ("في عملي اليومي لأتحرّك أسرع وأرى أكثر — مع بقاء المسؤولية والأخلاقيات والقرار النهائي بيد الإنسان.",
  "dans mon travail quotidien pour aller plus vite et voir plus loin — la responsabilité, l'éthique et la décision finale restant entre des mains humaines."),
"Faster Diagnostics": ("تشخيص أسرع","Diagnostic accéléré"),
"AI-assisted log and packet analysis surfaces patterns and anomalies in minutes instead of hours — then I verify every finding manually before acting.":
 ("تحليل السجلات والحزم بمساعدة الذكاء الاصطناعي يكشف الأنماط والشذوذ في دقائق بدل ساعات — ثم أتحقق من كل نتيجة يدوياً قبل التصرّف.",
  "L'analyse des logs et des paquets assistée par IA révèle motifs et anomalies en minutes plutôt qu'en heures — puis je vérifie chaque constat manuellement avant d'agir."),
"Configuration Review": ("مراجعة الإعدادات","Revue de configuration"),
"Automated cross-checking of firewall rules, ACLs and device configs against best practice, catching misconfigurations before they reach production.":
 ("مقارنة آلية لقواعد جدار الحماية وقوائم ACL وإعدادات الأجهزة مع أفضل الممارسات، لالتقاط الأخطاء قبل وصولها للإنتاج.",
  "Vérification automatisée des règles pare-feu, ACL et configurations face aux bonnes pratiques, pour détecter les erreurs avant la production."),
"Threat Awareness": ("الوعي بالتهديدات","Veille des menaces"),
"Continuous tracking of emerging vulnerabilities and attack techniques, summarized and mapped to what actually matters for your specific environment.":
 ("متابعة مستمرة للثغرات الناشئة وأساليب الهجوم، ملخّصة ومربوطة بما يهمّ بيئتك تحديداً.",
  "Suivi continu des vulnérabilités émergentes et des techniques d'attaque, synthétisé et rapporté à ce qui compte pour votre environnement."),
"Documentation & Reporting": ("التوثيق والتقارير","Documentation & Rapports"),
"Clear, structured handover documents and audit reports produced quickly — reviewed, corrected and signed off by me, never shipped raw.":
 ("وثائق تسليم وتقارير تدقيق واضحة ومنظّمة تُنجز بسرعة — أراجعها وأصحّحها وأعتمدها بنفسي، ولا تُسلَّم أبداً كما هي.",
  "Documents de livraison et rapports d'audit clairs et structurés, produits rapidement — relus, corrigés et validés par moi, jamais livrés bruts."),
"Automation": ("الأتمتة","Automatisation"),
"Scripted routine tasks — inventory, health checks, backup verification — so human attention goes where it's genuinely needed.":
 ("أتمتة المهام الروتينية — الجرد، وفحوص السلامة، والتحقق من النسخ الاحتياطي — ليتوجّه الانتباه البشري حيث يُحتاج فعلاً.",
  "Tâches routinières scriptées — inventaire, contrôles de santé, vérification des sauvegardes — pour concentrer l'attention humaine là où elle compte."),
"The Human Touch": ("اللمسة البشرية","La touche humaine"),
"AI advises; it doesn't decide. Every recommendation passes through context, experience and accountability before it reaches your network.":
 ("الذكاء الاصطناعي يقترح ولا يقرّر. كل توصية تمرّ عبر السياق والخبرة والمسؤولية قبل أن تصل إلى شبكتك.",
  "L'IA conseille, elle ne décide pas. Chaque recommandation passe par le contexte, l'expérience et la responsabilité avant d'atteindre votre réseau."),

# ---------- 06 project ----------
"06 — Graduation Project": ("٠٦ — مشروع التخرّج","06 — Projet de fin d'études"),
"Designing & securing": ("تصميم وتأمين","Concevoir et sécuriser"),
"an enterprise network": ("شبكة مؤسّسية","un réseau d'entreprise"),
"Completed": ("مُنجز","Terminé"),
"Graduation Project": ("مشروع تخرّج","Projet de fin d'études"),
"Final grade": ("العلامة النهائية","Note finale"),
"Practical Guide: Designing and Securing an Enterprise Network":
 ("دليل عملي: تصميم وتأمين شبكة مؤسّسية","Guide pratique : concevoir et sécuriser un réseau d'entreprise"),
"A complete, field-tested methodology for designing, securing and supervising a Local Area Network for an organization — from the first technical audit all the way to penetration testing and verification. Built on a real enterprise deployment using industry-standard tools (Cisco, pfSense, Zabbix) and fully simulated in GNS3, then generalized so it applies to any organization: a small company, an educational institution, or a local data center.":
 ("منهجية كاملة ومُختبرة ميدانياً لتصميم وتأمين ومراقبة شبكة محلية لمؤسسة — من أول تدقيق تقني وحتى اختبارات الاختراق والتحقق. مبنية على نشر مؤسسي حقيقي بأدوات معيارية (Cisco، pfSense، Zabbix) ومُحاكاة بالكامل في GNS3، ثم مُعمّمة لتنطبق على أي مؤسسة: شركة صغيرة، أو مؤسسة تعليمية، أو مركز بيانات محلي.",
  "Une méthodologie complète et éprouvée sur le terrain pour concevoir, sécuriser et superviser un réseau local d'entreprise — du premier audit technique jusqu'aux tests d'intrusion et à la validation. Bâtie sur un déploiement réel avec des outils standards (Cisco, pfSense, Zabbix), entièrement simulée sous GNS3, puis généralisée à toute organisation : PME, établissement d'enseignement ou centre de données local."),
"Work began with a full audit of the existing network — hardware inventory, traffic flows, logical architecture and a risk matrix combining likelihood and impact — which fed a requirements document tying every proposed control back to the CIA triad. From there: a hierarchical collapsed-core design, six departmental VLANs with a structured addressing plan, a pfSense firewall enforcing least privilege, defense in depth at Layers 2 and 3, real-time supervision, and finally validation through simulated attacks.":
 ("بدأ العمل بتدقيق شامل للشبكة القائمة — جرد الأجهزة، وتدفّقات حركة المرور، والبنية المنطقية، ومصفوفة مخاطر تجمع الاحتمال والأثر — وأفضى ذلك إلى وثيقة متطلبات تربط كل ضابط مقترح بثالوث السرية والسلامة والتوافر. ثم: تصميم هرمي بنواة مدمجة، وستة VLAN حسب الأقسام مع خطة عنونة منظّمة، وجدار حماية pfSense يفرض أقل الامتيازات، ودفاع متعدد الطبقات عند الطبقتين ٢ و٣، ومراقبة لحظية، وأخيراً تحقّق عبر هجمات محاكاة.",
  "Le travail a débuté par un audit complet du réseau existant — inventaire matériel, flux de trafic, architecture logique et matrice de risques croisant probabilité et impact — alimentant un cahier des charges reliant chaque mesure à la triade DIC. Ensuite : une architecture hiérarchique collapsed-core, six VLAN par département avec un plan d'adressage structuré, un pare-feu pfSense appliquant le moindre privilège, une défense en profondeur aux couches 2 et 3, une supervision temps réel et enfin une validation par attaques simulées."),
"Diagnosis": ("التشخيص","Diagnostic"),
"— hardware inventory, risk matrix, requirements document": ("— جرد الأجهزة، ومصفوفة المخاطر، ووثيقة المتطلبات","— inventaire matériel, matrice de risques, cahier des charges"),
"Architecture": ("البنية","Architecture"),
"— collapsed-core (Core L3 + Access L2), scalable by design": ("— نواة مدمجة (Core L3 + Access L2)، قابلة للتوسّع بالتصميم","— collapsed-core (Cœur L3 + Accès L2), évolutive par conception"),
"Segmentation": ("التقسيم","Segmentation"),
"— 6 VLANs (802.1Q), VLSM addressing, dedicated management VLAN 99": ("— ٦ شبكات VLAN (802.1Q)، وعنونة VLSM، وVLAN 99 مخصّص للإدارة","— 6 VLAN (802.1Q), adressage VLSM, VLAN 99 dédié à l'administration"),
"Stability": ("الاستقرار","Stabilité"),
"— Rapid-PVST+ with sub-two-second convergence on link failure": ("— Rapid-PVST+ بتقارب أقل من ثانيتين عند انقطاع الوصلة","— Rapid-PVST+ avec convergence sous deux secondes en cas de panne de lien"),
"Perimeter": ("المحيط","Périmètre"),
"— pfSense sub-interfaces, per-VLAN DHCP, NAT, default-deny rules": ("— واجهات pfSense الفرعية، وDHCP لكل VLAN، وNAT، وقواعد المنع الافتراضي","— sous-interfaces pfSense, DHCP par VLAN, NAT, règles deny par défaut"),
"Defense in depth": ("الدفاع المتعمّق","Défense en profondeur"),
"— extended ACLs, Port Security, DHCP Snooping, Dynamic ARP Inspection": ("— قوائم ACL موسّعة، وPort Security، وDHCP Snooping، وDynamic ARP Inspection","— ACL étendues, Port Security, DHCP Snooping, Dynamic ARP Inspection"),
"Access": ("الوصول","Accès"),
"— 802.1X/RADIUS with AAA, IPSec site-to-site and OpenVPN SSL (AES-256-GCM)": ("— 802.1X/RADIUS مع AAA، وIPSec بين المواقع، وOpenVPN SSL (AES-256-GCM)","— 802.1X/RADIUS avec AAA, IPSec site-à-site et OpenVPN SSL (AES-256-GCM)"),
"Supervision": ("الإشراف","Supervision"),
"— Zabbix on an isolated VLAN 50, SNMP + Syslog, triggers and dashboards": ("— Zabbix على VLAN 50 معزول، وSNMP + Syslog، ومحفّزات ولوحات متابعة","— Zabbix sur un VLAN 50 isolé, SNMP + Syslog, déclencheurs et tableaux de bord"),
"Validation — simulated attacks": ("التحقق — هجمات محاكاة","Validation — attaques simulées"),
"Nmap port scan": ("مسح منافذ Nmap","Scan de ports Nmap"),
"from an unauthorized VLAN → all ports": ("من VLAN غير مصرّح به ← كل المنافذ","depuis un VLAN non autorisé → tous les ports"),
"filtered": ("محجوبة","filtrés"),
"VLAN hopping": ("قفز VLAN","VLAN hopping"),
"against 802.1Q isolation →": ("ضد عزل 802.1Q ←","contre l'isolation 802.1Q →"),
"blocked": ("مُوقَف","bloqué"),
"ARP spoofing": ("انتحال ARP","Usurpation ARP"),
"(Ettercap) → rejected by Dynamic ARP Inspection": ("(Ettercap) ← مرفوض بواسطة Dynamic ARP Inspection","(Ettercap) → rejeté par Dynamic ARP Inspection"),
"MAC flooding": ("إغراق MAC","Inondation MAC"),
"(Macof) → port driven to": ("(Macof) ← المنفذ انتقل إلى","(Macof) → port basculé en"),
", users unaffected": ("، دون تأثّر المستخدمين",", utilisateurs non affectés"),
"Post-hardening measurements: internal RTT under 2 ms, STP failover under 2 s, firewall and monitoring CPU load held below 80% under deep packet inspection.":
 ("قياسات بعد التحصين: زمن ذهاب وإياب داخلي أقل من ٢ مللي ثانية، وتحويل STP أقل من ثانيتين، وحمل المعالج على جدار الحماية والمراقبة تحت ٨٠٪ أثناء الفحص العميق للحزم.",
  "Mesures après durcissement : RTT interne sous 2 ms, bascule STP sous 2 s, charge CPU pare-feu et supervision maintenue sous 80 % en inspection profonde de paquets."),

# ---------- 07 contact ----------
"07 — Contact": ("٠٧ — تواصل معي","07 — Contact"),
"Let's build something": ("لنبنِ شيئاً","Construisons quelque chose"),
"secure": ("آمناً","de sûr"),
"Available for network setup, security audits, IT support and consulting. Write below and it lands straight in my inbox.":
 ("متاح لتركيب الشبكات، والتدقيق الأمني، والدعم التقني، والاستشارات. اكتب أدناه وستصلني رسالتك مباشرة.",
  "Disponible pour l'installation réseau, les audits de sécurité, le support informatique et le conseil. Écrivez ci-dessous, le message arrive directement dans ma boîte."),
"New message": ("رسالة جديدة","Nouveau message"),
"From": ("من","De"),
"Email": ("البريد الإلكتروني","E-mail"),
"Subject": ("الموضوع","Objet"),
"Message": ("الرسالة","Message"),
"Send": ("إرسال","Envoyer"),
"Copy address": ("نسخ العنوان","Copier l'adresse"),
"Opens your mail app with everything filled in.": ("يفتح تطبيق البريد لديك وكل الحقول جاهزة.","Ouvre votre messagerie avec tout pré-rempli."),

# placeholders
"Your name": ("اسمك","Votre nom"),
"you@example.com": ("you@example.com","vous@exemple.com"),
"Network audit request": ("طلب تدقيق شبكة","Demande d'audit réseau"),
"Tell me about your network, size of the site, and what you need…":
 ("أخبرني عن شبكتك، وحجم الموقع، وما تحتاجه…","Parlez-moi de votre réseau, de la taille du site et de vos besoins…"),

# ---------- admin ----------
"Admin access": ("دخول المسؤول","Accès administrateur"),
"Enter your password to add, edit or remove links.": ("أدخل كلمة المرور لإضافة الروابط أو تعديلها أو حذفها.","Entrez votre mot de passe pour ajouter, modifier ou supprimer des liens."),
"Wrong password.": ("كلمة مرور خاطئة.","Mot de passe incorrect."),
"Unlock": ("فتح","Déverrouiller"),
"Password": ("كلمة المرور","Mot de passe"),
"Link manager": ("مدير الروابط","Gestionnaire de liens"),
"Add, edit, reorder or delete. Saved instantly in this browser.": ("أضف أو عدّل أو رتّب أو احذف. يُحفظ فوراً في هذا المتصفح.","Ajouter, modifier, réordonner ou supprimer. Enregistré instantanément dans ce navigateur."),
"Profile picture": ("الصورة الشخصية","Photo de profil"),
"Upload image": ("رفع صورة","Téléverser une image"),
"Restore default": ("استعادة الافتراضي","Rétablir par défaut"),
"Square image works best. Saved in this browser.": ("الصورة المربّعة هي الأنسب. تُحفظ في هذا المتصفح.","Une image carrée convient le mieux. Enregistrée dans ce navigateur."),
"Add a new link": ("إضافة رابط جديد","Ajouter un lien"),
"Other / Website": ("أخرى / موقع","Autre / Site web"),
"Add link": ("إضافة الرابط","Ajouter le lien"),
"Cancel edit": ("إلغاء التعديل","Annuler la modification"),
"Import": ("استيراد","Importer"),
"Change password": ("تغيير كلمة المرور","Changer le mot de passe"),
"Reset": ("إعادة تعيين","Réinitialiser"),
"Lock": ("قفل","Verrouiller"),
"Manage links": ("إدارة الروابط","Gérer les liens"),
"Label (e.g. GitHub)": ("التسمية (مثل GitHub)","Libellé (ex. GitHub)"),
"Handle / subtitle (e.g. @onyx)": ("المعرّف / وصف مختصر (مثل ‎@onyx)","Identifiant / sous-titre (ex. @onyx)"),
"Edit": ("تعديل","Modifier"),
"Remove": ("حذف","Supprimer"),
"Move up": ("تحريك لأعلى","Monter"),
"Move down": ("تحريك لأسفل","Descendre"),
"Close": ("إغلاق","Fermer"),
"Icon": ("الأيقونة","Icône"),
"Back to top": ("العودة للأعلى","Retour en haut"),

# ---------- footer / marquee ----------
"El Moattassam Billah Adem Ferrah — Network Administration & Security":
 ("المعتصم بالله آدم فرّاح — إدارة وأمن الشبكات","El Moattassam Billah Adem Ferrah — Administration & Sécurité Réseau"),
"Network Security": ("أمن الشبكات","Sécurité réseau"),
"VLAN Segmentation": ("تقسيم VLAN","Segmentation VLAN"),
"Firewall Hardening": ("تحصين جدار الحماية","Durcissement pare-feu"),
"AI Integration": ("دمج الذكاء الاصطناعي","Intégration IA"),
"Secure Design": ("تصميم آمن","Conception sécurisée"),
"IT Support": ("الدعم التقني","Support informatique"),
"Web Design": ("تصميم المواقع","Design web"),

# ---------- JS runtime strings ----------
"Community profile": ("الملف الشخصي","Profil communautaire"),
"Copied!": ("تم النسخ!","Copié !"),
"Copy": ("نسخ","Copier"),

"Welcome to my website \u2014 enter": ("\u0645\u0631\u062d\u0628\u0627\u064b \u0628\u0643 \u0641\u064a \u0645\u0648\u0642\u0639\u064a \u2014 \u0627\u062f\u062e\u0644","Bienvenue sur mon site \u2014 entrer"),
"Secure network topology: ISP to firewall, core switch, access switches, VLANs and server zone": ("\u0637\u0648\u0628\u0648\u0644\u0648\u062c\u064a\u0627 \u0634\u0628\u0643\u0629 \u0645\u0624\u0645\u064e\u0651\u0646\u0629: \u0645\u0646 \u0645\u0632\u0648\u0651\u062f \u0627\u0644\u062e\u062f\u0645\u0629 \u0625\u0644\u0649 \u062c\u062f\u0627\u0631 \u0627\u0644\u062d\u0645\u0627\u064a\u0629\u060c \u0641\u0627\u0644\u0645\u0628\u062f\u0651\u0644 \u0627\u0644\u0645\u0631\u0643\u0632\u064a\u060c \u0641\u0645\u0628\u062f\u0651\u0644\u0627\u062a \u0627\u0644\u0648\u0635\u0648\u0644 \u0648\u0634\u0628\u0643\u0627\u062a VLAN \u0648\u0645\u0646\u0637\u0642\u0629 \u0627\u0644\u062e\u0648\u0627\u062f\u0645","Topologie r\u00e9seau s\u00e9curis\u00e9e : FAI vers pare-feu, switch c\u0153ur, switchs d'acc\u00e8s, VLAN et zone serveurs"),

"Add, edit, reorder or delete. Then press Publish and upload site.json so every visitor sees the changes.": ("أضف أو عدّل أو رتّب أو احذف. ثم اضغط «نشر» وارفع ملف site.json ليراه كل الزوار.","Ajouter, modifier, réordonner ou supprimer. Puis cliquez sur Publier et téléversez site.json pour que tous les visiteurs voient les changements."),
"Square image works best. Included in site.json when you publish.": ("الصورة المربّعة هي الأنسب. تُضمَّن في ملف site.json عند النشر.","Une image carrée convient le mieux. Incluse dans site.json lors de la publication."),
"Publish (site.json)": ("نشر (site.json)","Publier (site.json)"),

"Cloud sync": ("مزامنة سحابية","Synchronisation cloud"),
"Off \u2014 changes stay on this device": ("متوقفة — التغييرات تبقى على هذا الجهاز","Inactive — les changements restent sur cet appareil"),
"Connect Supabase so every edit appears instantly for all visitors, on every device.": ("اربط Supabase ليظهر كل تعديل فوراً لجميع الزوار، على كل الأجهزة.","Connectez Supabase pour que chaque modification apparaisse instantanément pour tous les visiteurs, sur tous les appareils."),
"Connect & sync": ("ربط ومزامنة","Connecter & synchroniser"),
"Disconnect": ("قطع الاتصال","Déconnecter"),
"Project URL (https://xxxx.supabase.co)": ("رابط المشروع (https://xxxx.supabase.co)","URL du projet (https://xxxx.supabase.co)"),
"Anon public key": ("المفتاح العلني anon","Clé publique anon"),
"Admin password (for saving)": ("كلمة مرور المسؤول (للحفظ)","Mot de passe admin (pour enregistrer)"),
}