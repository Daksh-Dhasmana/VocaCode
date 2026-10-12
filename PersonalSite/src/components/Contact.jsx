export default function Contact() {
  const contactLinks = [
    {
      name: "GitHub",
      url: "https://github.com/Daksh-Dhasmana",
    },
    {
      name: "LinkedIn",
      url: "https://www.linkedin.com/in/daksh-dhasmana-548897277/",
    },
    {
      name: "Email",
      url: "mailto:dakshdhasmana@gmail.com",
    },
  ];

  return (
    <footer id="contact" className="bg-gradient-to-b from-gray-950 to-black text-white py-20 border-t border-gray-800/80">
      <div className="max-w-5xl mx-auto px-4 text-center">
        <p className="text-xs font-bold uppercase tracking-wider text-blue-400 mb-1">
          Connect
        </p>
        <h2 className="text-3xl sm:text-4xl font-extrabold mb-3 tracking-tight">
          Get In Touch
        </h2>
        <p className="text-gray-400 max-w-xl mx-auto mb-10 text-sm md:text-base leading-relaxed">
          Feel free to reach out for collaborations, project inquiries, or just to connect.
        </p>

        {/* Contact links */}
        <div className="flex flex-wrap justify-center gap-4 mb-14">
          {contactLinks.map((link, index) => (
            <a
              key={index}
              href={link.url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2.5 px-6 py-3 bg-gray-900/80 hover:bg-gray-800 border border-gray-800 hover:border-gray-700 text-gray-200 hover:text-white text-sm font-semibold rounded-xl shadow-sm hover:shadow-md transition-all duration-200 hover:-translate-y-0.5"
            >
              <span className="w-2 h-2 rounded-full bg-blue-500"></span>
              <span>{link.name}</span>
            </a>
          ))}
        </div>

        {/* Footer copyright */}
        <div className="border-t border-gray-900 pt-8 text-xs text-gray-500">
          &copy; {new Date().getFullYear()} Daksh Dhasmana. Built with React &amp; Tailwind CSS.
        </div>
      </div>
    </footer>
  );
}
