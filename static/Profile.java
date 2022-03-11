import java.util.List;

public class Profile {
    private String firstname;
    private String lastname;
    private String email;
    private String aboutMe;
    private String currentCompany;
    private List<String> professionTypes;
    private List<String> skills;
    private List<String> projects;
    private List<String> pastCompanies;

    public Profile (String firstname, 
                    String lastname, 
                    String email,
                    String aboutMe, 
                    String currentCompany, 
                    List<String> professionTypes, 
                    List<String> skills,
                    List<String> projects, 
                    List<String> pastCompanies) {
                        this.setFirstName(firstname);
                        this.setLastName(lastname);
                        this.setEmail(email);
                        this.setAboutMe(aboutMe);
                        this.setCurrentCompany(currentCompany);
                        this.setProfessionTypes(professionTypes);
                        this.setSkills(skills);
                        this.setProjects(projects);
                        this.setPastCompanies(pastCompanies);
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

    public void setProfessionTypes(List<String> professionTypes) {
        this.professionTypes = professionTypes;
    }

    public void addProfessionTypes(String professionTypes) {
        this.professionTypes.add(professionTypes);
    }

    public List<String> getProfessionTypes() {
        return this.professionTypes;
    }

    public void setSkills(List<String> skills) {
        this.skills = skills;
    }

    public void addSkill(String skill) {
        this.skills.add(skill);
    }

    public List<String> getSkills() {
        return this.skills;
    }

    public void setProjects(List<String> projects) {
        this.projects = projects;
    }

    public void addProject(String project) {
        this.projects.add(project);
    }

    public List<String> getProjects() {
        return this.projects;
    }

    public void setPastCompanies(List<String> pastCompanies) {
        this.pastCompanies = pastCompanies;
    }

    public void addPastCompany(String pastCompany) {
        this.pastCompanies.add(pastCompany);
    }

    public List<String> pastCompanies() {
        return this.pastCompanies;
    }
}