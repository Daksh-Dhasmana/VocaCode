export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 bg-gray-950/80 backdrop-blur-md border-b border-gray-800/80">
      <div className="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between">
        <a
          href="#home"
          className="text-xl font-bold tracking-tight text-white hover:text-blue-400 transition-colors"
        >
          Daksh <span className="text-blue-500">Dhasmana</span>
        </a>

        <div className="flex items-center space-x-1 sm:space-x-2 text-sm font-medium text-gray-400">
          <a
            href="#home"
            className="px-3 py-1.5 rounded-lg hover:text-white hover:bg-gray-900 transition-colors"
          >
            Home
          </a>
          <a
            href="#about"
            className="px-3 py-1.5 rounded-lg hover:text-white hover:bg-gray-900 transition-colors"
          >
            About
          </a>
          <a
            href="#skills"
            className="px-3 py-1.5 rounded-lg hover:text-white hover:bg-gray-900 transition-colors"
          >
            Skills
          </a>
          <a
            href="#projects"
            className="px-3 py-1.5 rounded-lg hover:text-white hover:bg-gray-900 transition-colors"
          >
            Projects
          </a>
          <a
            href="#contact"
            className="px-3 py-1.5 rounded-lg hover:text-white hover:bg-gray-900 transition-colors"
          >
            Contact
          </a>
        </div>
      </div>
    </nav>
  );
}
