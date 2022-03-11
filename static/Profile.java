public class Profile {
    private String firstname;
    private String lastname;
    private String email;
    private String aboutMe;
    private String currentCompany;
    private ArrayList<String> professionTypes;
    private ArrayList<String> skills;
    private ArrayList<String> projects;
    private ArrayList<String> pastCompanies;

    public Profile (String firstname, 
                    String lastname, 
                    String email,
                    String aboutMe, 
                    String currentCompany, 
                    ArrayList<String> professionTypes, 
                    ArrayList<String> skills,
                    ArrayList<String> projects, 
                    ArrayList<String> pastCompanies) {
                        this.
                    }

    public void setFirstName(String firstname) {
        this.firstname = firstname;
    }

    public String getFirstName() {
        return this.firstname;
    }

    public void setLastName(String lastname) {
        this.lastname = lastname;
    }

    public String getlastName() {
        return this.lastname;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEmail() {
        return this.email;
    }

    public void setAboutMe(String aboutMe) {
        this.aboutMe = aboutMe;
    }

    public String getAboutMe() {
        return this.aboutMe;
    }

    public void setCurrentCompany(String currentCompany) {
        this.currentCompany = currentCompany;
    }

    public String getCurrentCompany() {
        return this.currentCompany;
    }

    public void setProfessionTypes(ArrayList<String> professionTypes) {
        this.professionTypes = professionTypes;
    }

    public void addProfessionTypes(String professionTypes) {
        this.professionTypes.add(professionTypes);
    }

    public ArrayList<String> getProfessionTypes() {
        return this.professionTypes;
    }

    public void setSkills(ArrayList<String> skills) {
        this.skills = skills;
    }

    public void addSkill(String skill) {
        this.skills.add(skill);
    }

    public ArrayList<String> getSkills() {
        return this.skills;
    }

    public void setProjects(ArrayList<String> projects) {
        this.projects = projects;
    }

    public void addProject(String project) {
        this.projects.add(project);
    }

    public ArrayList<String> getProjects() {
        return this.projects;
    }

    public void setPastCompanies(ArrayList<String> pastCompanies) {
        this.pastCompanies = pastCompanies;
    }

    public void addPastCompany(String pastCompany) {
        this.pastCompanies.add(pastCompany);
    }

    public ArrayList<String> pastCompanies() {
        return this.pastCompanies;
    }
}