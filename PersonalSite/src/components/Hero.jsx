import profileImg from "../assets/profile.jpg";

export default function Hero() {
  return (
    <section id="home" className="py-16 md:py-24 bg-gray-950 border-b border-gray-800/80">
      <div className="max-w-5xl mx-auto px-4 flex flex-col-reverse md:flex-row items-center justify-between gap-12">
        
        {/* Intro Text */}
        <div className="flex-1 text-center md:text-left">
          {/* Status Badge */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold tracking-wide uppercase mb-4">
            <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
            Available for Opportunities
          </div>

          <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-white mb-4">
            Hi, I'm{" "}
            <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
              Daksh Dhasmana
            </span>
          </h1>

          <p className="text-lg md:text-xl text-gray-300 font-normal leading-relaxed mb-6">
            Final-year B.Tech CSE student &amp; Front-End Web Developer who builds responsive, component-driven web applications using React, JavaScript, and modern CSS.
          </p>

          {/* About / Bio Card */}
          <div
            id="about"
            className="p-5 bg-gradient-to-b from-gray-900 to-gray-900/60 rounded-xl border border-gray-800 shadow-lg mb-8"
          >
            <h2 className="text-xs font-bold uppercase tracking-wider text-blue-400 mb-1.5">
              About Me
            </h2>
            <p className="text-gray-300 text-sm md:text-base leading-relaxed">
              Passionate about building clean user interfaces and transitioning into backend development, data structures, and system design.
            </p>
          </div>

          {/* CTA Links */}
          <div className="flex flex-wrap justify-center md:justify-start gap-4">
            <a
              href="#projects"
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white text-sm font-semibold rounded-lg shadow-lg shadow-blue-600/25 transition-all hover:-translate-y-0.5"
            >
              View Projects
            </a>
            <a
              href="#contact"
              className="px-6 py-3 bg-gray-900 hover:bg-gray-850 text-gray-200 hover:text-white text-sm font-semibold rounded-lg border border-gray-700/80 transition-all hover:-translate-y-0.5 shadow-sm"
            >
              Contact Me
            </a>
          </div>
        </div>

        {/* Profile Image with subtle ambient glow ring */}
        <div className="flex-shrink-0">
          <div className="relative group">
            {/* Ambient backlight glow */}
            <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-full blur-md opacity-30 group-hover:opacity-50 transition duration-300"></div>

            {/* Profile Avatar */}
            <div className="relative w-44 h-44 sm:w-52 sm:h-52 md:w-56 md:h-56 rounded-full overflow-hidden border-2 border-gray-700/80 shadow-2xl bg-gray-900 flex items-center justify-center">
              <img
                src={profileImg}
                alt="Daksh Dhasmana"
                className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300"
              />
            </div>
          </div>
        </div>

      </div>
    </section>
  );
}
