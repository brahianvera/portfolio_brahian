class parts_templates:

    def all_parts(self):
        parts = {}
        parts["menu"] = self.menu()
        return parts

    def menu(self):
        return """
                <nav id="menu" class="panel">
                    <ul>
                        <li>
                            <a href="index.html">Home</a>
                        </li>
                        <li>
                            <a href="about.html" class="active">About</a>
                        </li>
                        <!-- <li>
                            <a href="skills.html">Skills</a>
                        </li> -->
                        <li>
                            <a href="services.html">Services</a>
                        </li>
                        <li>
                            <a href="portfolio.html">Portofolio</a>
                        </li>
                        <li>
                            <a href="contact.html">contact</a>
                        </li>
                    </ul>
                </nav>
            """
