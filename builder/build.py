#!/usr/bin/env python3
"""
Tinderbox Installer Builder

Generates Tinderbox installer files from YAML definitions.
"""

import yaml
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


class TinderboxInstallerBuilder:
    def __init__(self, definitions_dir: Path):
        self.definitions_dir = definitions_dir
        self.workspace = None
        self.prototypes = None
        self.templates = None
        self.functions = None
        
    def load_definitions(self):
        """Load all YAML definition files."""
        try:
            with open(self.definitions_dir / "workspace.yaml") as f:
                self.workspace = yaml.safe_load(f)
                
            with open(self.definitions_dir / "prototypes.yaml") as f:
                self.prototypes = yaml.safe_load(f)
                
            with open(self.definitions_dir / "templates.yaml") as f:
                self.templates = yaml.safe_load(f)
                
            with open(self.definitions_dir / "functions.yaml") as f:
                self.functions = yaml.safe_load(f)
                
        except FileNotFoundError as e:
            print(f"Error: Definition file not found: {e}")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            sys.exit(1)
            
    def validate_definitions(self) -> bool:
        """Validate the loaded definitions."""
        errors = []
        
        # Check workspace structure
        if not self.workspace or 'workspace' not in self.workspace:
            errors.append("workspace.yaml must contain 'workspace' section")
            
        # Check prototypes
        if not self.prototypes or 'prototypes' not in self.prototypes:
            errors.append("prototypes.yaml must contain 'prototypes' section")
            
        # Check templates
        if not self.templates or 'templates' not in self.templates:
            errors.append("templates.yaml must contain 'templates' section")
            
        # Check functions
        if not self.functions or 'library_modules' not in self.functions:
            errors.append("functions.yaml must contain 'library_modules' section")
            
        if errors:
            for error in errors:
                print(f"Validation Error: {error}")
            return False
            
        print("✅ All definitions validated successfully")
        return True
        
    def generate_header(self) -> str:
        """Generate the installer file header."""
        workspace_info = self.workspace['workspace']
        return f"""// {workspace_info['name']} - Generated Installer
// {workspace_info['description']}
// Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// Copy this entire code to a note's $Rule attribute and set $RuleDisabled=false

"""

    def generate_log_setup(self) -> str:
        """Generate log note creation."""
        log_config = self.workspace['workspace']['log']
        
        code = f"""// Create log note
create("{log_config['path']}");
$Badge("{log_config['path']}") = "{log_config['badge']}";
$TextFont("{log_config['path']}") = "{log_config['font']}";
$TextFontSize("{log_config['path']}") = {log_config['font_size']};
$Text("{log_config['path']}") = "=== {self.workspace['workspace']['name']} Installation ===\\n";

$Text("{log_config['path']}") = $Text("{log_config['path']}") + "Starting installation...\\n";

"""
        return code
        
    def generate_folder_structure(self) -> str:
        """Generate basic folder structure."""
        code = "// Create basic structure\n"
        
        for folder in self.workspace['workspace']['folders']:
            code += f'create("{folder["path"]}");\n'
            code += f'$Badge("{folder["path"]}") = "{folder["badge"]}";\n'
            
            if 'prototype' in folder:
                code += f'$Prototype("{folder["path"]}") = "{folder["prototype"]}";\n'
                
            if 'onAdd' in folder:
                code += f'$OnAdd("{folder["path"]}") = "{folder["onAdd"]}";\n'
                
            code += "\n"
            
        code += '$Text("/Log") = $Text("/Log") + "Created basic folder structure\\n";\n\n'
        return code
        
    def generate_functions(self) -> str:
        """Generate library function modules."""
        code = ""
        
        for module in self.functions['library_modules']:
            code += f'// Create {module["name"]} module\n'
            code += f'create("{module["path"]}");\n'
            
            # Generate function text
            function_code = ""
            for func in module['functions']:
                params = ", ".join(func['params'])
                function_code += f"function {func['name']}({params}) {{\n"
                
                # Indent function body
                body_lines = func['body'].strip().split('\n')
                for line in body_lines:
                    if line.strip():
                        function_code += f"   {line}\n"
                    else:
                        function_code += "\n"
                        
                function_code += "}\n\n"
            
            # Escape quotes in function code
            escaped_code = function_code.replace("'", "\\'")
            code += f'$Text("{module["path"]}") = \'{escaped_code}\';\n'
            
            code += f'$Badge("{module["path"]}") = "{module["badge"]}";\n'
            code += f'$Searchable("{module["path"]}") = {str(module["searchable"]).lower()};\n'
            code += f'$SmartQuotes("{module["path"]}") = {str(module["smartQuotes"]).lower()};\n\n'
            
        return code
        
    def generate_templates(self) -> str:
        """Generate HTML export templates."""
        code = "// Create Templates folder and basic templates\n"
        
        for template in self.templates['templates']:
            code += f'create("{template["path"]}");\n'
            
            # Convert template content to proper format
            content = template['content'].strip()
            content = content.replace('\n', '\\n')
            
            code += f'$Text("{template["path"]}") = "{content}";\n'
            code += f'$Badge("{template["path"]}") = "{template["badge"]}";\n'
            
        return code + "\n"
        
    def generate_prototypes(self) -> str:
        """Generate prototype definitions."""
        code = "// Create Prototypes folder and basic prototypes\n"
        
        for prototype in self.prototypes['prototypes']:
            code += f'create("{prototype["path"]}");\n'
            code += f'$Badge("{prototype["path"]}") = "{prototype["badge"]}";\n'
            code += f'$HTMLExportTemplate("{prototype["path"]}") = "{prototype["template"]}";\n'
            
            if 'displayedAttributes' in prototype:
                code += f'$DisplayedAttributes("{prototype["path"]}") = "{prototype["displayedAttributes"]}";\n'
                
            code += f'$IsPrototype("{prototype["path"]}") = {str(prototype["isPrototype"]).lower()};\n'
            
        return code + "\n"
        
    def generate_attributes(self) -> str:
        """Generate custom attribute creation."""
        code = "// Create user attributes\n"
        
        for attr in self.workspace['workspace']['attributes']:
            code += f'createAttribute("{attr["name"]}", "{attr["type"]}");\n'
            
        code += "\n// Set up custom attributes for prototypes\n"
        
        for prototype in self.prototypes['prototypes']:
            if 'defaultAttributes' in prototype:
                for attr_name, attr_value in prototype['defaultAttributes'].items():
                    code += f'${attr_name}("{prototype["path"]}") = "{attr_value}";\n'
                    
        return code + "\n"
        
    def generate_css_styles(self) -> str:
        """Generate CSS styles - this could be moved to a definition file too."""
        return """// Create CSS style
create("/Hints/Preview/style");
$Text("/Hints/Preview/style") = "body{font-family:Helvetica,Arial,sans-serif;margin-left:7.5%;margin-right:7.5%;line-height:1.4;color:#333;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "h1,h2,h3,h4,h5,h6{color:#2c3e50;margin-top:1.5em;margin-bottom:0.5em;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "table{margin:2em 0;font-size:0.9em;border:1px solid #888;border-collapse:collapse;width:100%;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "td,th{padding:0.5em;border:1px solid #ddd;text-align:left;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "th{background-color:#f5f5f5;font-weight:bold;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "img{width:100%;height:auto;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "code{background-color:#f8f8f8;padding:2px 4px;border-radius:3px;}";
$Text("/Hints/Preview/style") = $Text("/Hints/Preview/style") + "pre{background-color:#f8f8f8;padding:1em;border-radius:5px;overflow-x:auto;}";
$Searchable("/Hints/Preview/style") = false;

"""

    def generate_footer(self) -> str:
        """Generate installation completion and cleanup."""
        workspace_info = self.workspace['workspace']
        return f"""$Text("/Log") = $Text("/Log") + "Created complete function library\\n";
$Text("/Log") = $Text("/Log") + "- CoreUtils: Basic utilities and helpers\\n";
$Text("/Log") = $Text("/Log") + "- ProjectBuilder: Full project structure automation\\n";
$Text("/Log") = $Text("/Log") + "- TemplateBuilder: HTML export templates\\n";
$Text("/Log") = $Text("/Log") + "- CSS Styles: Ready for HTML export\\n";
$Text("/Log") = $Text("/Log") + "\\n";
$Text("/Log") = $Text("/Log") + "READY TO USE:\\n";
$Text("/Log") = $Text("/Log") + "1. Create notes in /Projects - they auto-build structure\\n";
$Text("/Log") = $Text("/Log") + "2. Functions available globally from /Hints/Library/\\n";
$Text("/Log") = $Text("/Log") + "3. CSS ready for HTML export templates\\n";
$Text("/Log") = $Text("/Log") + "\\n";
$Text("/Log") = $Text("/Log") + "{workspace_info['name']} installation completed successfully!\\n";

// Disable rule
$RuleDisabled = true;
"""

    def build_installer(self) -> str:
        """Build the complete installer from all components."""
        installer = ""
        installer += self.generate_header()
        installer += self.generate_log_setup()
        installer += self.generate_folder_structure()
        installer += self.generate_functions()
        installer += self.generate_templates()
        installer += self.generate_prototypes()
        installer += self.generate_attributes()
        installer += self.generate_css_styles()
        installer += self.generate_footer()
        
        return installer
        

def main():
    parser = argparse.ArgumentParser(description='Build Tinderbox installer from definitions')
    parser.add_argument('-o', '--output', default='actions/generated-installer.txt',
                       help='Output file path')
    parser.add_argument('--validate', action='store_true',
                       help='Only validate definitions, don\'t build')
    parser.add_argument('--definitions', default='builder/definitions',
                       help='Path to definitions directory')
    
    args = parser.parse_args()
    
    # Initialize builder
    definitions_path = Path(args.definitions)
    if not definitions_path.exists():
        print(f"Error: Definitions directory not found: {definitions_path}")
        sys.exit(1)
        
    builder = TinderboxInstallerBuilder(definitions_path)
    
    # Load and validate
    print("Loading definitions...")
    builder.load_definitions()
    
    if not builder.validate_definitions():
        sys.exit(1)
        
    if args.validate:
        print("Validation complete - definitions are valid!")
        return
        
    # Build installer
    print("Building installer...")
    installer_code = builder.build_installer()
    
    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(installer_code)
        
    print(f"✅ Generated installer: {output_path}")
    print(f"📊 {len(installer_code.splitlines())} lines, {len(installer_code)} characters")


if __name__ == "__main__":
    main()