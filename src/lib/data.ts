/* Single source of truth for all site content. Every fact comes from Ashok H's resume. */

import { asset } from "./asset";

export const PROFILE = {
  name: "Ashok H",
  firstName: "Ashok",
  initials: "AH",
  role: "Software Engineer",
  heroTitle: "Software Engineer",
  dept: "Engineering",
  company: "ConnectSecure",
  since: "Feb 2026",
  location: "Bengaluru, India",
  email: "ashok.anjinappa@campusuvce.in",
  phone: "+91 9741854203",
  phoneHref: "tel:+919741854203",
  github: "https://github.com/AshokTechie",
  linkedin: "https://www.linkedin.com/in/ashok-h-75a0b82a9",
  resume: asset("/cv.pdf"),
  resumeSummary:
    "Proactive and detail-oriented Software Engineer with hands-on enterprise experience in developing responsive web applications and scalable microservices. Proficient in Angular 20, TypeScript, Python (Flask), and Azure cloud infrastructure (AKS, Cosmos DB). Proven ability in building real-time IoT monitoring dashboards, processing telemetry data, and optimizing frontend performance, with strong problem-solving skills across the full software development lifecycle, from UI design to containerized CI/CD deployments.",
} as const;

export type SectionId = "about" | "skills" | "work" | "certifications" | "experience" | "achievements" | "contact";

/** Section tag numbers follow rendered order. Use as `${index} — ${label}`. */
export const SECTIONS: Record<SectionId, { index: string; label: string }> = {
  about: { index: "01", label: "About me" },
  skills: { index: "02", label: "Skills" },
  work: { index: "03", label: "Selected work" },
  certifications: { index: "04", label: "Coursework & Foundations" },
  experience: { index: "05", label: "Experience" },
  achievements: { index: "06", label: "Honours & metrics" },
  contact: { index: "07", label: "Contact" },
};

export interface NavItem {
  id: SectionId;
  label: string;
  index: string;
}
export const NAV: NavItem[] = (["about", "skills", "work", "experience", "achievements", "contact"] as const).map((id) => ({
  id,
  index: SECTIONS[id].index,
  label: id === "work" ? "Work" : id[0].toUpperCase() + id.slice(1),
}));

/* ---------- Skills ---------- */
export type SkillFamily = "Languages" | "Frameworks" | "Databases" | "Tools & Cloud" | "Foundations";

export interface Skill {
  /** Logo key for <TechLogo name=... /> (brand file in /public/logos or a concept icon). */
  logo: string;
  name: string;
  family: SkillFamily;
  /** Unique 2-letter element symbol. */
  symbol: string;
  /** Atomic number: 1-based position in the whole table. */
  number: number;
  /** Where the resume says it was used. Absent when the resume doesn't say. */
  usedIn?: string[];
}
export interface SkillGroup {
  family: SkillFamily;
  skills: Skill[];
}

type RawSkill = Omit<Skill, "number" | "family">;

const RAW: Record<SkillFamily, RawSkill[]> = {
  Languages: [
    { logo: "python", name: "Python", symbol: "Py", usedIn: ["Microservices, Modbus IoT router & telemetry rule engine, ConnectSecure", "Conversational AI Agent – Agentic RAG System", "Smart Agriculture ML System", "Car Rental Platform"] },
    { logo: "typescript", name: "TypeScript", symbol: "Ts", usedIn: ["Enterprise dashboard development, ConnectSecure", "Angular 20 reactive UI state & strict typing"] },
    { logo: "javascript", name: "JavaScript", symbol: "Js", usedIn: ["Frontend and Node.js backend development", "Car Rental Platform (React.js, Node.js)"] },
    { logo: "cpp", name: "C++", symbol: "Cp", usedIn: ["Core Engineering Coursework, Data Structures & Algorithms, UVCE"] },
    { logo: "c", name: "C", symbol: "Cl", usedIn: ["Low-level Systems Programming, Operating Systems, UVCE"] },
    { logo: "java", name: "Java", symbol: "Ja", usedIn: ["Object Oriented Programming, UVCE"] },
    { logo: "sql", name: "SQL", symbol: "Sq", usedIn: ["Relational queries, transactional data and schema modeling"] },
  ],
  Frameworks: [
    { logo: "angular", name: "Angular 20", symbol: "Ng", usedIn: ["Scalable real-time CGD monitoring dashboards across hundreds of BPCL Retail Outlets, ConnectSecure"] },
    { logo: "react", name: "React.js", symbol: "Re", usedIn: ["Interactive frontend component architecture, Car Rental Platform"] },
    { logo: "flask", name: "Flask", symbol: "Fl", usedIn: ["Python microservices & Flask-SocketIO telemetry streaming, ConnectSecure"] },
    { logo: "fastapi", name: "FastAPI", symbol: "Fa", usedIn: ["High-performance asynchronous REST API microservices"] },
    { logo: "nodejs", name: "Node.js", symbol: "Nd", usedIn: ["Modular REST API backend with 12+ endpoints and JWT auth, Car Rental Platform"] },
    { logo: "express", name: "Express.js", symbol: "Ex", usedIn: ["REST API routing, middleware and RBAC, Car Rental Platform"] },
    { logo: "langgraph", name: "LangGraph", symbol: "Lg", usedIn: ["Agentic pipeline with conditional routing, state management and 5 decoupled nodes"] },
    { logo: "langchain", name: "LangChain", symbol: "Lc", usedIn: ["Conversational AI agent workflows and document processing"] },
    { logo: "tailwindcss", name: "Tailwind CSS", symbol: "Tw", usedIn: ["Modern utility-first responsive web interfaces"] },
  ],
  Databases: [
    { logo: "cosmosdb", name: "Azure Cosmos DB", symbol: "Co", usedIn: ["Cloud database infrastructure for live telemetry and CGD operations, ConnectSecure"] },
    { logo: "qdrant", name: "Qdrant", symbol: "Qd", usedIn: ["Vector database for semantic similarity search with sub-200ms latency on 50+ documents"] },
    { logo: "mongodb", name: "MongoDB", symbol: "Mo", usedIn: ["NoSQL document persistence, Car Rental Platform"] },
    { logo: "mysql", name: "MySQL", symbol: "My", usedIn: ["Relational database management and query optimization"] },
    { logo: "firebase", name: "Firebase", symbol: "Fb", usedIn: ["Time-series store processing 100+ sensor readings/minute, Smart Agriculture ML System"] },
  ],
  "Tools & Cloud": [
    { logo: "aks", name: "Azure AKS", symbol: "Ak", usedIn: ["Zero-downtime multi-cluster Azure Kubernetes Service releases (DEV, QA, PROD), ConnectSecure"] },
    { logo: "docker", name: "Docker", symbol: "Do", usedIn: ["Containerized microservices deployments, ConnectSecure & Car Rental Platform"] },
    { logo: "azure-devops", name: "Azure DevOps", symbol: "Ad", usedIn: ["Containerized CI/CD release pipelines across multi-cluster AKS, ConnectSecure"] },
    { logo: "gcp", name: "Google Cloud (GCP)", symbol: "Gc", usedIn: ["Predictive analytics ML model hosting and inference pipeline, Smart Agriculture"] },
    { logo: "azureiot", name: "Azure IoT", symbol: "Ai", usedIn: ["Modbus register ingestion and IoT telemetry microservices, ConnectSecure"] },
    { logo: "git", name: "Git", symbol: "Gi", usedIn: ["Structured feature branching and version control management across all codebases"] },
    { logo: "github", name: "GitHub", symbol: "Gh", usedIn: ["Collaborative development, code review workflows and CI/CD automation"] },
    { logo: "linux", name: "Linux", symbol: "Li", usedIn: ["Container hosts, server environments and microservice deployment runtimes"] },
    { logo: "postman", name: "Postman", symbol: "Pm", usedIn: ["REST API testing, endpoint contract verification and debugging"] },
    { logo: "gemini", name: "Gemini API", symbol: "Gm", usedIn: ["Grounded AI response generation with prompt engineering and voice I/O"] },
  ],
  Foundations: [
    { logo: "medal", name: "Data Structures & Algorithms", symbol: "Ds", usedIn: ["Core Coursework, UVCE - Algorithmic complexity, trees, graphs and dynamic programming"] },
    { logo: "medal", name: "Computer Networks", symbol: "Cn", usedIn: ["Core Coursework, UVCE - OSI layers, TCP/IP, WebSockets and network security"] },
    { logo: "medal", name: "Operating Systems", symbol: "Os", usedIn: ["Core Coursework, UVCE - Concurrency, threads, memory management and file systems"] },
    { logo: "medal", name: "Object Oriented Programming", symbol: "Oo", usedIn: ["Core Coursework, UVCE - Encapsulation, inheritance, polymorphism and design patterns"] },
  ],
};

export const SKILL_FAMILIES = Object.keys(RAW) as SkillFamily[];

let atomic = 0;
export const SKILL_GROUPS: SkillGroup[] = SKILL_FAMILIES.map((family) => ({
  family,
  skills: RAW[family].map((s) => ({ ...s, family, number: ++atomic })),
}));
export const SKILLS: Skill[] = SKILL_GROUPS.flatMap((g) => g.skills);

/* ---------- Experience & education ---------- */
export interface ExperienceItem {
  id: string;
  role: string;
  company: string;
  period: string;
  bullets: string[];
}
export const EXPERIENCE: ExperienceItem[] = [
  {
    id: "connectsecure",
    role: "Software Engineer",
    company: "ConnectSecure",
    period: "Feb 2026 – Present",
    bullets: [
      "Architected scalable real-time monitoring dashboards using Angular 20, PrimeNG, and ApexCharts to track City Gas Distribution (CGD) operations, visualizing live CNG dispenser sales, line pressures, and mass flow meter (MFM) telemetry across hundreds of BPCL Retail Outlets (ROs).",
      "Integrated WebSockets and optimized Angular change-detection, enabling live geospatial alert streaming while eliminating UI thread blocking and screen freeze during high-frequency telemetry bursts and modal dialog interactions.",
      "Implemented IoT router and telemetry rule engine microservices in Python, ingesting raw Modbus register payloads, accurately resolving Retail Outlet IDs (ROIDs), and automating safety threshold and emergency shutdown alerts.",
      "Developed the Station-level Gas Reconciliation & Custody Transfer Billing Engine, automating multi-unit volume conversions (kg, SCM, MMBTU), flagging custody imbalance penalty breaches (≤90% / ≥110%), and generating provisional billing PDF statements.",
      "Designed dynamic administrative tooling, including high-performance searchable autocomplete filters for retail outlets, custom date-range analytical queries, and interactive Modbus register mapping interfaces for rapid device onboarding.",
      "Collaborated on containerized CI/CD deployments using Docker and Azure DevOps pipelines, ensuring automated, zero-downtime releases across multi-cluster Azure Kubernetes Service (AKS) environments (DEV, QA, PROD).",
    ],
  },
];

export interface EducationItem {
  id: string;
  school: string;
  degree: string;
  place?: string;
  period?: string;
  cgpa?: string;
  pursuing?: boolean;
}
export const EDUCATION: EducationItem[] = [
  {
    id: "uvce",
    school: "University of Visvesvaraya College of Engineering (UVCE)",
    degree: "B.Tech – Electronics & Communication Engineering",
    place: "Bengaluru, India",
    period: "2022 – 2026",
    cgpa: "CGPA: 8.76",
  },
];

export interface TimelineItem {
  id: string;
  kind: "education" | "work";
  org: string;
  title: string;
  place?: string;
  period: string;
  pursuing?: boolean;
  bullets?: string[];
}
const edu = (id: string): EducationItem => EDUCATION.find((e) => e.id === id)!;
const job = (id: string): ExperienceItem => EXPERIENCE.find((e) => e.id === id)!;
const fromEdu = (e: EducationItem): TimelineItem => ({
  id: e.id,
  kind: "education",
  org: e.school,
  title: `${e.degree}${e.cgpa ? ` (${e.cgpa})` : ""}`,
  place: e.place,
  period: e.pursuing ? "Currently pursuing" : (e.period ?? ""),
  pursuing: e.pursuing,
});
const fromJob = (e: ExperienceItem): TimelineItem => ({
  id: e.id,
  kind: "work",
  org: e.company,
  title: e.role,
  period: e.period,
  bullets: e.bullets,
});

export const TIMELINE: TimelineItem[] = [
  fromEdu(edu("uvce")),
  fromJob(job("connectsecure")),
];

/* ---------- Projects ---------- */
export interface ProjectTech {
  name: string;
  logo?: string;
}
export interface Project {
  id: string;
  number: string;
  title: string;
  date: string;
  kicker: string;
  description: string;
  bullets: string[];
  features: string[];
  tech: ProjectTech[];
  link?: { href: string; label: string };
  visual: "blog" | "voice" | "iot";
}

export const PROJECTS: Project[] = [
  {
    id: "rag",
    number: "01",
    title: "Conversational AI Agent – Agentic RAG System",
    date: "2024",
    kicker: "Agentic RAG & LangGraph",
    description:
      "Built a system that takes a goal (answer a question about a PDF), breaks it into steps (retrieve relevant chunks, reason over context, synthesize answer), and recovers gracefully when a retrieval step returns poor results.",
    bullets: [
      "Designed a LangGraph agentic pipeline with conditional routing, state management, and 5 decoupled nodes – ingestion, chunking, embedding, retrieval, and generation – each independently testable and replaceable.",
      "Implemented document chunking and HuggingFace embedding generation; stored vectors in Qdrant for semantic similarity search, achieving sub-200ms retrieval latency on 50+ indexed documents.",
      "Connected Gemini API for grounded response generation with prompt engineering and output validation; added speech recognition and synthesis for full voice I/O workflow.",
      "Built automated evaluation workflows covering 20+ test scenarios; measured retrieval accuracy and response quality against benchmark sets, achieving 95%+ accuracy – iterated prompts based on results.",
    ],
    features: [
      "LangGraph agentic pipeline",
      "Conditional routing & state management",
      "5 decoupled testable nodes",
      "HuggingFace embedding generation",
      "Qdrant vector similarity search (<200ms)",
      "Gemini API grounded generation",
      "Full voice I/O workflow",
      "Automated evaluation (95%+ accuracy)",
    ],
    tech: [
      { name: "Python", logo: "python" },
      { name: "LangGraph", logo: "langgraph" },
      { name: "LangChain", logo: "langchain" },
      { name: "Qdrant", logo: "qdrant" },
      { name: "HuggingFace" },
      { name: "Gemini API", logo: "gemini" },
    ],
    link: { href: "https://github.com/AshokTechie", label: "View on GitHub" },
    visual: "voice",
  },
  {
    id: "agri",
    number: "02",
    title: "Smart Agriculture ML System",
    date: "2024",
    kicker: "IoT & Predictive ML Pipeline",
    description:
      "Built and deployed Python ML models on GCP for predictive analytics on real agricultural sensor data, achieving 85%+ prediction accuracy on held-out validation sets.",
    bullets: [
      "Built and deployed Python ML models on GCP for predictive analytics on real agricultural sensor data, achieving 85%+ prediction accuracy on held-out validation sets.",
      "Designed the full data pipeline: ESP32 sensor collection → REST API ingestion → Firebase time-series store → GCP inference → mobile delivery, processing 100+ readings/minute with zero data loss.",
      "Compared model approaches and tuned for accuracy vs. latency trade-offs; integrated model outputs via REST API with sub-2 second end-to-end latency under live competition load.",
    ],
    features: [
      "Predictive analytics on sensor data",
      "85%+ prediction accuracy on held-out sets",
      "ESP32 hardware sensor collection",
      "Firebase time-series store",
      "GCP inference & model serving",
      "100+ readings/minute with zero data loss",
      "Sub-2s latency under competition load",
      "Mobile REST API delivery",
    ],
    tech: [
      { name: "Python", logo: "python" },
      { name: "GCP", logo: "gcp" },
      { name: "Firebase", logo: "firebase" },
      { name: "ESP32" },
    ],
    link: { href: "https://github.com/AshokTechie", label: "View on GitHub" },
    visual: "iot",
  },
  {
    id: "rental",
    number: "03",
    title: "Car Rental Platform",
    date: "2023",
    kicker: "Full-Stack Microservices Platform",
    description:
      "Designed a modular REST API backend with 12+ endpoints, JWT authentication, role-based access control, and structured error handling and logging throughout – built to be readable and maintainable by other engineers.",
    bullets: [
      "Designed a modular REST API backend with 12+ endpoints, JWT authentication, role-based access control, and structured error handling and logging throughout – built to be readable and maintainable by other engineers.",
      "Managed codebase with Git across structured feature branches; containerised with Docker; maintained full technical documentation – zero defects post-deployment.",
    ],
    features: [
      "Modular REST API with 12+ endpoints",
      "JWT authentication & RBAC",
      "Structured error handling & logging",
      "Git structured feature branches",
      "Containerised with Docker",
      "Zero defects post-deployment",
      "Full technical documentation",
    ],
    tech: [
      { name: "Node.js", logo: "nodejs" },
      { name: "Express.js", logo: "express" },
      { name: "React.js", logo: "react" },
      { name: "MongoDB", logo: "mongodb" },
      { name: "Docker", logo: "docker" },
      { name: "Python", logo: "python" },
    ],
    link: { href: "https://github.com/AshokTechie", label: "View on GitHub" },
    visual: "blog",
  },
];

/* ---------- Certifications & Coursework ---------- */
export interface Certification {
  id: string;
  index: string;
  title: string;
  date: string;
  url: string;
  issuer?: string;
}
const CERT_RAW: Omit<Certification, "index">[] = [
  { id: "ds", title: "Data Structures & Algorithms", issuer: "UVCE Core Engineering", date: "2023", url: "#skills" },
  { id: "oop", title: "Object Oriented Programming", issuer: "UVCE Core Engineering", date: "2023", url: "#skills" },
  { id: "cn", title: "Computer Networks", issuer: "UVCE Core Engineering", date: "2024", url: "#skills" },
  { id: "os", title: "Operating Systems", issuer: "UVCE Core Engineering", date: "2024", url: "#skills" },
  { id: "ai-deploy", title: "End-to-End AI System Deployment Award", issuer: "Competition Award", date: "2024", url: "#achievements" },
  { id: "btech", title: "B.Tech in Electronics & Communication (CGPA: 8.76)", issuer: "UVCE Bengaluru", date: "2022 – 2026", url: "#about" },
];
export const CERTIFICATIONS: Certification[] = CERT_RAW.map((c, i) => ({ ...c, index: String(i + 1).padStart(2, "0") }));

/* ---------- Achievements ---------- */
export interface Achievement {
  id: string;
  index: string;
  label: string;
  caption: string;
  detail: string;
  logo: string;
  tint: string;
  number?: number;
  prefix?: string;
  suffix?: string;
  unit?: string;
}
const ACH_RAW: Omit<Achievement, "index">[] = [
  {
    id: "competition",
    label: "Competition AI Award",
    caption: "Shipped an end-to-end AI system with real sensor data",
    detail: "Deployed ML models under live competition load",
    logo: "medal",
    tint: "rgba(237,28,36,0.16)",
  },
  {
    id: "rag-acc",
    label: "Agentic RAG Accuracy",
    caption: "Benchmark evaluation accuracy across 20+ test scenarios",
    detail: "LangGraph pipeline with retrieval quality validation",
    logo: "langgraph",
    tint: "rgba(233,69,96,0.16)",
    number: 95,
    suffix: "%",
  },
  {
    id: "vector-latency",
    label: "Sub-200ms Retrieval",
    caption: "Vector similarity search latency on 50+ indexed documents",
    detail: "Qdrant vector store with HuggingFace embeddings",
    logo: "qdrant",
    tint: "rgba(220,38,38,0.16)",
    number: 200,
    prefix: "<",
    unit: "ms latency",
  },
  {
    id: "ml-acc",
    label: "Predictive ML Accuracy",
    caption: "Sensor predictive analytics on held-out validation sets",
    detail: "Python models deployed on GCP for real-time agricultural data",
    logo: "gcp",
    tint: "rgba(66,133,244,0.16)",
    number: 85,
    suffix: "%",
  },
  {
    id: "telemetry",
    label: "Zero-Loss Telemetry",
    caption: "Readings processed per minute with zero data loss",
    detail: "ESP32 to REST API to Firebase time-series stream",
    logo: "firebase",
    tint: "rgba(255,160,0,0.18)",
    number: 100,
    suffix: "+",
    unit: "readings / min",
  },
  {
    id: "latency",
    label: "End-to-End Latency",
    caption: "REST API response time under live competition load",
    detail: "Full pipeline: sensor ingestion, cloud store, and ML inference",
    logo: "python",
    tint: "rgba(55,118,171,0.16)",
    number: 2,
    prefix: "<",
    suffix: "s",
    unit: "latency",
  },
  {
    id: "cgpa",
    label: "Academic Distinction",
    caption: "B.Tech in Electronics & Communication Engineering",
    detail: "University of Visvesvaraya College of Engineering (UVCE)",
    logo: "uvce",
    tint: "rgba(26,54,93,0.16)",
    number: 8.76,
    unit: "/ 10 CGPA",
  },
];
export const ACHIEVEMENTS: Achievement[] = ACH_RAW.map((a, i) => ({ ...a, index: String(i + 1).padStart(2, "0") }));
