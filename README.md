# Update Zenodo to recognize existing GitHub releases

Simple Python script to request [Zenodo][1] through its web API for recognizing
pre-existing releases of [GitHub][2] based projects when they have only been
added to Zenodo **after** a release (or multiple) has been published to GitHub.

## Usage

Assuming you'll try to generate Zenodo DOIs for a project (repository) called
**`aweseomproject`** that is located in the GitHub organization
**`exampleorg`**:

* Create a settings file by copying the `settings/example.yml` to a new one, say
  `settings/aweseomproject.yml`
* Adjust the `repo` field to read `exampleorg/aweseomproject`
* Use a web browser and navigate to
  <https://github.com/exampleorg/aweseomproject/settings/hooks>
* Hit the `Edit` button next to the Zenodo webhook
* From the `Payload URL` field copy the last part (everything after
  `access_token=`)
* Place that string in the `token` entry of the newly copied settings file
* Save the new settings file

Finally, run the script by specifying the path to the new settings file:

```Python
python update-zenodo.py settings/aweseomproject.yml
```

[1]: https://zenodo.org
[2]: https://github.com
